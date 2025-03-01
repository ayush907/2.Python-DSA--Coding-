import numpy as np
import matplotlib.pyplot as plt

def gradient_descent(x, y):
    learning_rate = 0.01
    iterations = 10000
    w = 0
    b = 0
    
    m = x.shape[0]  
    cost_lst = list()
    w_lst = list()
    b_lst = list()
    for i in range(iterations):

        y_pred = w * x + b

        cost = (1/m) * np.sum((y_pred - y) ** 2)

        dw = (2/m) * np.sum((y_pred - y) * x)
        db = (2/m) * np.sum(y_pred - y)

        w = w - (learning_rate * dw)
        b = b - (learning_rate * db)

        cost_lst.append(cost)
        w_lst.append(w)
        b_lst.append(b)


        print(f"iteration: {i} cost: {cost}  w: {w}   b: {b}")

    min_cost = np.nanmin(cost_lst)
    a = cost_lst.index(min_cost)
    min_w = w_lst[a]
    min_b = b_lst[a]

    print(a)
    print(f"the final minimum cost is {min_cost}")
    print(f"the final minimum weight is {min_w}")
    print(f"the final minimum bias is {min_b}")

    return min_w, min_b



x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 7, 9, 11, 13])

w, b = gradient_descent(x, y)
y_pred = w * x + b

plt.scatter(x,y)
plt.plot(x, y_pred, color='red')
plt.show()

import numpy as np

def gradient_descent_two(x, y):

    m, n = x.shape
    iteration = 10000
    learning_rate = 0.01
    w = np.array([0] * n)
    # w = np.zeros(n)
    b = 0

    cost_lst = list()

    w_list = list()
    b_list = list()
    for i in range(iteration):

        y_pred = np.dot(x, w.T) + b

        cost = (1/m) * np.sum((y_pred - y) ** 2)

        dw = (2/m) * np.dot(x.T, (y_pred - y))   
        db = (2/m) * np.sum(y_pred - y)

        w = w - learning_rate * dw
        b = b - learning_rate * db

        cost_lst.append(cost)
        w_list.append(w)
        b_list.append(b)

        print(f"iter: {i}  cost : {cost}   w: {w}   b: {b}")
    
    a = cost_lst.index(min(cost_lst))
    final_cost = min(cost_lst)
    final_weights = w_list[a]
    final_bias = b_list[a]

    print(a)
    print(f"final_cost : {final_cost}")
    print(f"final_weights : {final_weights}")
    print(f"final_bias : {final_bias}")


    


x = np.array([[1, 2],  
              [2, 3],  
              [3, 4],
              [4, 5],  
              [5, 6]]) 

y = np.array([5, 7, 9, 11, 13])  

gradient_descent_two(x, y)

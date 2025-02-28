
def counting_sort(arr):
    
    maximum = max(arr)   # step 1: arr ka max find karo

    aux_arr = [0] * (maximum + 1)  # step 2: maximum + 1 size ka ek auxillary array banao

    # for i in range(len(aux_arr)):  
    #     aux_arr[i] = 0

    for j in range(len(arr)):
        aux_arr[arr[j]] = aux_arr[arr[j]] + 1

    temp = -1
    for k in range(len(aux_arr)):
        while aux_arr[k] != 0:
            temp = temp + 1
            arr[temp] = k
            aux_arr[k] = aux_arr[k] - 1

    print(arr)

arr = [3,4,2,5,1]
counting_sort(arr)
            




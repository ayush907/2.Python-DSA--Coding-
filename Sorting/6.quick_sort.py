
def partition(arr, low, high):

    pivot = arr[high]   #calculating the pivot
    i = low - 1
    
    for j in range(low, high):
        if(arr[j] <= pivot):
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    i = i + 1
    arr[i], arr[high] = arr[high], arr[i]    

    return i



def quick_sort(arr, low, high):
    if low < high:
        pidx = partition(arr, low, high)
        quick_sort(arr, low, pidx - 1)
        quick_sort(arr, pidx + 1, high)


arr = [3,4,2,5,1]
quick_sort(arr, 0, len(arr)-1)
print(arr)

def selecton_sort(arr):
    for i in range(len(arr)):
        small = arr[i]
        pos = i
        for j in range(i+1, len(arr)):
            if small > arr[j]:
                pos = j
        arr[i], arr[pos] = arr[pos], arr[i]
        small, arr[pos] = small, arr[i]

    print(arr)

arr = [3,4,2,5,1]
selecton_sort(arr)
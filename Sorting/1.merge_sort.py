
def conquer(arr, low, mid, high):

    merged = [0] * (high - low + 1)

    x = 0
    idx1 = low        # tracks the left array index
    idx2 = mid + 1    # tracks the right array index

    while idx1 <= mid and idx2 <= high:
        if arr[idx1] <= arr[idx2]:
            merged[x] = arr[idx1]
            idx1 = idx1 + 1
        else:
            merged[x] = arr[idx2]
            idx2 = idx2 + 1
        x = x + 1

    # loop for copying the remaining elements of left array
    while idx1 <= mid:
        merged[x] = arr[idx1]
        idx1 = idx1 + 1
        x = x + 1

    # loop for copying the remaining elements of right array
    while idx2 <= high:
        merged[x] = arr[idx2]
        idx2 = idx2 + 1
        x = x + 1

    # copying the merged elements into the original array
    for i in range(len(merged)):
        arr[low + i] = merged[i]




def divide(arr, low, high):  # low: 0th index, high: last index (len(arr)-1)
    if low >= high:
        return
    
    mid = (low + high) // 2
    divide(arr, low, mid)
    divide(arr, mid + 1, high)
    conquer(arr, low, mid, high)
    

arr = [3,4,2,5,1]
divide(arr, 0, len(arr) - 1)
print(arr)

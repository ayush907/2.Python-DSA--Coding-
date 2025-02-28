
def heapify(arr, n, i):
    
    largest = i

    left_child_idx = 2 * i + 1
    right_child_idx = 2 * i + 2

    if left_child_idx < n and  arr[left_child_idx] > arr[largest]:
        largest = left_child_idx

    if right_child_idx < n and arr[right_child_idx] > arr[largest]:
        largest = right_child_idx

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n , largest)

def heap_sort(arr):
    n = len(arr)
    # tree mai neeche se heap banaani shuru karenge (last level ke ek upar vaale level se)
    for i in range(n//2,-1, -1):
        heapify(arr, n, i)
    # heap ke top(root) value ko tree ki last value se swap karenge orr fir tree mai upar se dobaara heap banaayenge
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


arr = [3,4,2,5,1]
print(f"before array: {arr}")
heap_sort(arr)
print(f"after sorting array: {arr}")

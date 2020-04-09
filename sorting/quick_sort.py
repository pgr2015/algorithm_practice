import numpy

def quickSortRecursive1(arr, low, high):
    if low >= high:
        return
    pivot = arr[low]
    left, right = low, high
    while left < right:
        while left < right and arr[right] > pivot:
            right -= 1
        arr[left] = arr[right]
        while left < right and arr[left] <= pivot:
            left += 1
        arr[right] = arr[left]
    arr[right] = pivot
    quickSortRecursive(arr, low, right - 1)
    quickSortRecursive(arr, right + 1, high)

def quickSortRecursive2(arr, low, high):
    if low >= high:
        return
    mid = partition(arr, low, high)
    quickSortRecursive2(arr, low, mid - 1)
    quickSortRecursive2(arr, mid + 1, high)

def partition(arr, low, high):
    pivot = arr[low]
    mid = low
    for i in range(low, high+1):
        if arr[i] < pivot:
            mid += 1
            arr[mid], arr[i] = arr[i], arr[mid]
    arr[low], arr[mid] = arr[mid], arr[low]
    return mid

test_case = numpy.random.randint(-100,100,size=50)
quickSortRecursive2(test_case, 0, len(test_case) - 1)
print(test_case)
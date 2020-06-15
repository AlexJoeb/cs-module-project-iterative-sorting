import math

def linear_search(arr, target):
    for i in range(0, len(arr), 1):
        item = arr[i]
        if item == target:
            return i
        else: continue
    return -1


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        middle = start + (end - start) // 2
        middle_value = arr[middle]

        if middle_value == target:
            return middle
        elif target < middle_value:
            end = middle - 1
        else:
            start = middle + 1

    return -1

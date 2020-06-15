# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # -> loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # -> save a reference of the current smallest value index
        smallest_index = i
        # -> iterate through all the values AFTER the current index
        for index in range(i, len(arr)):
            # -> if current value being checked is less than the current smallest index, save a reference to it.
            if arr[index] < arr[smallest_index]:
                smallest_index = index

        # -> Swap them.
        buff = arr[i]
        arr[i] = arr[smallest_index]
        arr[smallest_index] = buff

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    for x in range(0, len(arr) - 1, 1):
        for y in range(len(arr) - 1):
            if arr[y] > arr[y + 1]:
                buff = arr[y]
                arr[y] = arr[y + 1]
                arr[y + 1] = buff
    return arr

'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr

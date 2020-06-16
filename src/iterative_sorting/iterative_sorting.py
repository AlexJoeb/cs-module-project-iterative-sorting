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

# O(n) Runtime? Because it has to loops over everything in the array 2 times.
def count_sort(arr, maximum=None):
    # Initalize a dictionary so that we can hold the amount of times
    #   an interger is seen in arr.
    counts = {}
    # Initalize final array to be return after sort.
    final = []

    # For each element in arr, check to see if it is in counts. If not, itialize and +1.. else just +1 the existing element in counts.
    for n in arr:
        if n < 0:
            return "Error, negative numbers not allowed in Count Sort"
        if n not in counts:
            counts[n] = 0
        counts[n] += 1
        
    # Map over counts and add n to final count times.
    for n, count in sorted(counts.items()):
        for i in range(count):
            final.append(n)
    
    # Return final.
    return final
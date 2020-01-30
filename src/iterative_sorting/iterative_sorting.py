# Selction sort - first select min value in array and move it to far left,
# then select 2nd smallest value in array and move it to index [1]
# then select 3rd smallest value in array and move it to index [2]
# etc..

# Example: [3, 2, 4, 1]
# 1. [1, 2, 4, 3] => 1 and 3 are swapped because 1 is min
# 2. [1, 2, 4, 3] => 2 is in right place
# 3. [1, 2, 3, 4] => 3 and 4 swap because 3 is 3rd smallest value

# PLANNING:
# Need an inner loop
# Find the smallest element in the entire loop and place it at index[0]. Swap values.
# Find the next smallest element and place it at index[1]. Swap values.
# etc...


def selection_sort(arr):
    for x in range(0, len(arr) - 1):  # -1 since we start at index 0
        print("arr", arr)
        # print("x", x)
        # cur_index = x (?)
        # smallest_index = cur_index (?)
        # Inner loop is the "function" we are having the loop do to compare values when the array is being looped through
        # x+1 to check the index value to the right of x
        for next_value in range(x+1, len(arr)):
            # TO-DO: find next smallest element
            # (hint, can do in 3 loc)
            # Compare values - if next_value to the rightis smaller, then swap x and next_value indexes
            if arr[next_value] < arr[x]:
                arr[x], arr[next_value] = arr[next_value], arr[x]  # swap

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr

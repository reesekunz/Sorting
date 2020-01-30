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
        print("selection sort arr", arr)
        print("selection sort outer loops", x)
        # cur_index = x (?)
        # smallest_index = cur_index (?)
        # Inner loop is the "function" we are having the loop do to compare values when the array is being looped through
        # x+1 to check the index value to the right of x

        # TO-DO: find next smallest element (hint, can do in 3 loc)
        for y in range(x+1, len(arr)):
            print("selection sort inner loop", y)
            # Compare values - if next_value to the right is smaller, then swap x and next_value indexes
            if arr[y] < arr[x]:
                arr[x], arr[y] = arr[y], arr[x]  # swap

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    for x in range(0, len(arr)-1):  # -1 since we start at index 0 - outer loop
        # print("bubble sort arr", arr)
        # print("bubble sort outer loops", x)
        # inner loop. - x because we know the max value is already sorted at the end because they get 'bubbled'
        for y in range(0, len(arr)-1 - x):
            # print("bubble sort inner loop", y)
            # compare pair of elements. if current index value > next index value, swap.
            if arr[y] > arr[y+1]:
                arr[y], arr[y+1] = arr[y+1], arr[y]

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr

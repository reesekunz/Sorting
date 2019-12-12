# Iterative sorting - not a fast sorting algorithm because uses nested loops, useful for small data sets only, runs in O(n^2)


# Selction sort - first select min value in array and move it to far left,
# then select 2nd smallest value in array and move it to index [1]
# then select 3rd smallest value in array and move it to index [2]
# etc..

# Example: [3, 2, 4, 1]
# 1. [1, 2, 4, 3] => 1 and 3 are swapped because 1 is min
# 2. [1, 2, 4, 3] => 2 is in right place
# 3. [1, 2, 3, 4] => 3 and 4 swap because 3 is 3rd smallest value


def selection_sort(Array):
     # Outer loop tells us to continue iterating over array until everything is sorted in correct order
    for x in range(0, (len(Array) - 1)):  # -1 since we start at index 0
        # print("Array x", Array)
        # Inner loop is the "function" we are having the loop do to compare values when the array is being looped through
        for y in range(x+1, len(Array)):  # x+1 to check the index value to the right of x
            # print("Array y", Array)
            # Compare values - if value to the right (y) is smaller, then swap x and y indexes
            if Array[y] < Array[x]:
                Array[x], Array[y] = Array[y], Array[x]

    return Array


#Array = [3, 2, 4, 1]
#print("Selection sort", selection_sort(Array))


# Bubble sort - Compare first pair of elements. If right value > left value, swap. Else, do nothing.
# iterate through array, comparing other pairs of adjacent index values
# go back to beginning of array and repeat process until no swaps are needed
# (Max & higher values get bubbled to the end of the array)

# Example: [3, 2, 4, 1]

# 1. [3, 2] => [2, 3]
#   [3, 4] ok
#   [4, 1] => [1, 4]

#2. [2, 3, 1, 4]
#   [2, 3] ok
#   [3, 1] => [1, 3]
#   [3, 4] ok

#3   [2, 1, 3, 4]
#   [2, 1] => [1, 2]
#   [1, 3] ok
#   [3, 4] ok

#4   [1, 2, 3, 4]

def bubble_sort(Array):
    # Outer loop tells us to continue iterating over array until everything is sorted in correct order
    for x in range(0, (len(Array)-1)):  # -1 since we start at index 0
       # print("Array x", Array)
        # Inner loop is the "function" we are having the loop do to compare values when the array is being looped through
        for y in range(0, (len(Array)-1-x)):  # -x because "x" is the number of time the array has been looped through, so we know that x (the max value in the last index since it got bubbled) is already correctly sorted and can be subtracted from the length
           # print("Array y", Array)
            # compare value (y) to value on right(y +1). if value on left is larger, swap places
            if Array[y] > Array[y+1]:
                Array[y], Array[y+1] = Array[y+1], Array[y]

    return Array


#Array = [3, 2, 4, 1]
#print("Bubble sort", bubble_sort(Array))


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr

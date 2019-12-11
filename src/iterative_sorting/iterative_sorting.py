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
    # outer loop - goes from 0 to second to last item in list
    for x in range(0, (len(Array) - 1)):
        currentMinIndex = x
        # inner loop - iterates through unsorted part of outer loop
        for valueToRight in range(x+1, len(Array)):
            if Array[valueToRight] < Array[currentMinIndex]:  # save index of min item and compare
                currentMinIndex = valueToRight
        if currentMinIndex != x:
            # swap value into correct place (if needed)
            Array[x], Array[currentMinIndex] = Array[currentMinIndex], Array[x]

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
    for x in range(0, (len(Array)-1)):  # outer loop
        # inner loop (the last item in the list is already sorted so can do - x)
        for y in range(0, (len(Array)-1-x)):
            # compare value (y) to value on right(y +1). if value on left is larger, swap places
            if Array[y] > Array[y+1]:
                Array[y], Array[y+1] = Array[y+1], Array[y]

    return Array


#Array = [3, 2, 4, 1]
#print("Bubble sort", bubble_sort(Array))


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr

# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrayA, arrayB):
    elements = len(arrayA) + len(arrayB)
    merged_array = [0] * elements
    leftSide = 0
    rightSide = 0

    for x in range(0, elements):
        if leftSide >= len(arrayA):
            merged_array[x] = arrayB[rightSide]
            rightSide += 1

        elif rightSide >= len(arrayB):
            merged_array[x] = arrayA[leftSide]
            leftSide += 1
        elif arrayA[leftSide] < arrayB[rightSide]:
            merged_array[x] = arrayA[leftSide]
            leftSide += 1
        else:
            merged_array[x] = arrayB[rightSide]
            rightSide += 1
    return merged_array

# ANOTHER ALTERNATIVE - using pop instead of moving index +1
    # def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements

    # for x in range(merged_arr):
    # First we want to check if what we are comparing is empty. Then do the comparisons

    # 3. left side is empty
    # copy right side to add to merged_arr

    # 4. right side is empty
    # copy left side to add to merged_arr

    # 1. front of left side < front of right side
    # merged_arr[x] = arrA[0]
    # arrA.pop(0)  # get rid of front of array A after you add it

# 2. front of right side < front of left side
    # merged_arr[x] = arrB[0]
    # arrB.pop(0)  # get rid of front of array B after you add it

    # return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
# helper function - breaks larger function merge into smaller pieces
# Merge sort - breaks arrays in half until it len(list) = 1
def merge_sort(arr):
    if len(arr) > 1:  # base case - means it sorted
        return arr

    else:  # recursive case
        middle = int(len(arr) // 2)
        # break down into smaller lists again until gets to base case
        leftSide = merge_sort(arr[:middle])
        rightSide = merge_sort(arr[middle:])
        # merging two sorted arrays when it gets to this part
        merge(leftSide, rightSide)

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr

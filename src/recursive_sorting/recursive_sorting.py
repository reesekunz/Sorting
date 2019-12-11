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


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(array):
    if len(array) > 1:
        middle = int(len(array) // 2)
        leftSide = merge_sort(array[0:middle])
        rightSide = merge_sort(array[middle:])
        array = merge(leftSide, rightSide)
    return array


#Array = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
#print("Merge sort", merge_sort(Array))

# def merge_sort(Array):
#   merge_sort2(Array, 0, len((Array)-1))


# def merge_sort2(Array, first, last):
#     if first < last:
#         middle = (first + last) // 2
#         merge_sort2(Array, first, middle)
#         merge_sort2(Array, middle + 1, last)
#         merge(Array, first, middle, last)


# def merge(Array, first, middle, last):
#     Left = Array[first:middle+1]
#     Right = Array[middle+1:last+1]
#     array = merge(Left, Right)
#     Left = Right = 0

#     return array


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

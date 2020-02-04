from book import Book
import time
import csv

# O(n^2) - as number of books (input) increases, run time increases even faster. Not good. Not good.
# Nested loops is causing this slow run time.


# def insertion_sort(books):
#     # PLANNING:
#         # value at index 0 = sorted list of 1 book
#         # loop over value from index 1 to length of array
#             # compare value to left hand side.
#             # while value is smaller than value to the left, swap values. - need a nested loop because we are repeating steps within another process (the outer loop)
#             # if at front OR value is not smaller, go to end of loop
#     for x in range(1, len(books)):
#         y = x
#         # if value is smaller than one to the left, then swap places. y > 0 is just making sure were not at the front of list
#         while y > 0 and books[y].title < books[y-1].title:
#             # swap
#             temp = books[y]
#             books[y] = books[y-1]
#             books[y-1] = temp
#             y -= 1  # decrement by 1
#     return books


def insertion_sort(books):
    for x in range(1, len(books)):
        for next_value in range(x+1, len(books)):
            if books[next_value].title < books[x].title:
                books[x], books[next_value] = books[next_value], books[x]  # swap

    return books

# Version A: Conventional, recursive Quick Sort


def quick_sort_A(books):
    # base case - list of 1 = return list
    if len(books) <= 1:  # less than cause could have something empty on left or right side
        return books

    # recursive case
        # choose pivot (first element)
        # smaller elements go to left, larger elements go to the right
        # repeat process by picking a new pivot
        # quick_sort(LHS) + [pivot] + quick_sort(RHS)
    else:
        pivot = books[0].title
        left_side = [x for x in books[1:] if x.title <= pivot]
        # [1:] so you dont include the pivot
        right_side = [x for x in books[1:] if x.title > pivot]

        return quick_sort_A(left_side) + [pivot] + quick_sort_A(right_side)


# Version B:
# NOT done in place because for large inputs, we
# exceed Python's maximum recursion depth with
# in-place Quick Sort
def quick_sort_B(books):
    # STRETCH: implement Quick Sort for larger datasets

    return books


def book_sort(books):
    # STRETCH: combine Insertion & Quick Sort for
    # an improved sorting algorithm

    return books


# Read in book data from CSV file
# provided by https://github.com/uchidalab/book-dataset
with open('book_data.csv', encoding='utf8') as csvfile:
    my_books_long = []
    data = csv.DictReader(csvfile)
    for book in data:
        #print(book['title'], book['author'], book['genre'])
        my_books_long.append(
            Book(book['title'], book['author'], book['genre']))
    my_books_medium = my_books_long[0:997]
    my_books_short = my_books_long[0:10]

print("***********~Test with 10 Books~**********")
start = time.time()
sorted_books = insertion_sort(my_books_short)
end = time.time()
print("Insertion Sort took:  " + str((end - start)*1000) + " milliseconds")

# start = time.time()
# sorted_books = quick_sort_A(my_books_short, 0, len(my_books_short))
# end = time.time()
# print("Quick Sort (A) took:  " + str((end - start)*1000) + " milliseconds")


print("\n***********~Test with ~1,000 Books~**********")
start = time.time()
sorted_books = insertion_sort(my_books_medium)
end = time.time()
print("Insertion Sort took:  " + str((end - start)*1000) + " milliseconds")

# start = time.time()
# sorted_books = quick_sort_A(my_books_medium, 0, len(my_books_medium))
# end = time.time()
# print("Quick Sort (A) took:  " + str((end - start)*1000) + " milliseconds")


print("\n**********~Test with +2,000 Books~**********")
start = time.time()
sorted_books = insertion_sort(my_books_long)
end = time.time()
print("Insertion Sort took:  " + str((end - start)*1000) + " milliseconds")

# start = time.time()
# sorted_books = quick_sort_B(my_books_long)
# end = time.time()
# print("Quick Sort (B) took:  " + str((end - start)*1000) + " milliseconds")

# start = time.time()
# sorted_books = book_sort(my_books_long)
# end = time.time()
# print("Book Sort took:       " + str((end - start)*1000) + " milliseconds\n")

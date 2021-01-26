# ********************************************************************* #
# This file contains utility functions for sorting algorithms           #
# ********************************************************************* #
from random import randrange
import time
from prettytable import PrettyTable
from sort import recursive_sort
from sort import iterative_sort


# Creates a list of rnadom order unique values from 0 to n
def createRandList(n):
    values = [val for val in range(n)]
    array = []

    for val in range(n):
        array.append(values.pop(randrange(0, len(values))))

    return array


# Creates a list of ordered values from 0 to n
def createSortedList(n):
    return [val for val in range(n)]


# Creates a list of reverse ordered values from n to 0
def createRevSortedList(n):
    return [val for val in range(n-1, -1, -1)]


# Checks if an array is sorted
def is_sorted(array):
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return False
    return True


# Creates pretty table of timing data for each sorting algorithm
# in both iterative and recursive methods with different arrays
# (Sorted (best), Reverse sorted (worst) and Random order (average))
def createSortTimeData(algorithms, arrays):

    timeTable = PrettyTable(["(Random, Sorted, R-Sorted)ms"] + algorithms)

    iterative_methods = {
            'bubbleSort': iterative_sort.bubbleSort,
            'quickSort': iterative_sort.quickSort,
            'heapSort': iterative_sort.heapSort,
            'mergeSort': iterative_sort.mergeSort,
        }

    recursive_methods = {
            'bubbleSort': recursive_sort.bubbleSort,
            'quickSort': recursive_sort.quickSort,
            'heapSort': recursive_sort.heapSort,
            'mergeSort': recursive_sort.mergeSort,
        }

    table = [['Iterative'],
             ['Recursive']]

    for sort in algorithms:

        iterative_values = []
        recursive_values = []
        for array in arrays:
            lst = array[:]
            tic = time.perf_counter()
            iterative_methods[sort](lst)
            toc = time.perf_counter()

            iterative_values.append((toc - tic) * 100)

            lst = array[:]
            tic = time.perf_counter()
            if sort == 'bubbleSort':
                recursive_methods[sort](lst, len(lst))
            elif sort == 'quickSort':
                recursive_methods[sort](lst, 0, len(lst) - 1)
            else:
                recursive_methods[sort](lst)
            toc = time.perf_counter()

            recursive_values.append((toc - tic) * 1000)

        # generate iterative row
        table[0].append(f"({', '.join([str(round(val, 4)) for val in iterative_values])})ms")
        # generate recursive row
        table[1].append(f"({', '.join([str(round(val, 4)) for val in recursive_values])})ms")

    # add rows to table
    for row in range(2):
        timeTable.add_row(table[row])

    # print pretty table to console
    print(timeTable)

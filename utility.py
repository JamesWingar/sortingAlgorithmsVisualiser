# ********************************************************************* #
# This file contains utility functions for sorting algorithms           #
# ********************************************************************* #
from random import randrange


def createRandList(n):
    values = [val for val in range(n)]
    array = []

    for val in range(n):
        array.append(values.pop(randrange(0, len(values))))

    return array


def is_sorted(array):
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return False
    return True

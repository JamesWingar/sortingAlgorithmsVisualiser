# ********************************************************************* #
# This file contains four sorting algorithms using the iterative method #
# ********************************************************************* #

# iterative merge sort implementaion
def mergeSort(array):
    return array


# iterative merge sort implementaion
def bubbleSort(array):

    for j in range(len(array)):
        swap_count = 0
        for i in range(len(array) - j - 1):
            if array[i] > array[i + 1]:
                array[i + 1], array[i] = array[i], array[i + 1]
                '''
                temp = array[i+1]
                array[i+1] = array[i]
                array[i] = temp
                '''
                swap_count = 1

        # if iterate without swap, then sorted
        if swap_count == 0:
            break

    return array


# iterative quick sort implementaion
def quickSort(array):
    return array


# iterative heap sort implementaion
def heapSort(array):
    return array

# ********************************************************************* #
# This file contains four sorting algorithms using the recursive method #
# ********************************************************************* #

# recursive merge sort implementaion
def mergeSort(array):

    if len(array) <= 1:  # exit condition
        return array

    left, middle, right = 0, len(array) // 2, len(array)

    left_array = mergeSort(array[left:middle])
    right_array = mergeSort(array[middle:right])

    return merge(left_array, right_array)  # merge two arrays


def merge(left_array, right_array):
    merged = []

    # append the smallest value from l or r arrays
    while len(left_array) > 0 and len(right_array) > 0:
        if left_array[0] > right_array[0]:
            merged.append(right_array.pop(0))
        else:
            merged.append(left_array.pop(0))

    # add anything remaining in arrays
    if len(left_array) > 0:
        merged += left_array
    elif len(right_array) > 0:
        merged += right_array

    return merged


# recursive merge sort implementaion
def bubbleSort(array, n):

    if n <= 1:
        return array

    swap_count = 0
    # print(n - 1)
    for i in range(n - 1):
        if array[i] > array[i + 1]:
            array[i + 1], array[i] = array[i], array[i + 1]
            swap_count = 1

    if swap_count == 0:
        n = 0

    return bubbleSort(array, n - 1)


# recursive quick sort implementaion
def quickSort(array, low, high):

    if low < high:
        # find pivot point
        part = partition(array, low, high)
        quickSort(array, low, part)
        quickSort(array, part + 1, high)

    return array


def partition(array, low, high):
    # Hoare implementation
    pivot = array[(low + high) // 2]
    i = low - 1
    j = high + 1

    # for loop to limit the number of iterations
    for n in range(0, len(array)):
        # find an element less than pivot value
        i += 1
        while(array[i] < pivot):
            i += 1
        # find an element more than pivot value
        j -= 1
        while(array[j] > pivot):
            j -= 1
        # return if indexes crossover
        if i >= j:
            return j

        array[i], array[j] = array[j], array[i]


# recursive heap sort implementaion
def heapSort(array):
    n = len(array)

    # heapify to build tree
    for i in range(len(array)//2 - 1, -1, -1):
        array = heapify(array, n, i)

    # remove largest element
    for i in range(n-1, 0, -1):
        array[0], array[i] = array[i], array[0]
        array = heapify(array, i, 0)

    return array


def heapify(array, n, parent):
    largest = parent
    left_child = 2 * parent + 1
    right_child = 2 * parent + 2

    # check if left child is greater than parent
    if left_child < n and array[left_child] > array[largest]:
        largest = left_child
    # check if right child is greater than parent
    if right_child < n and array[right_child] > array[largest]:
        largest = right_child

    if largest != parent:
        array[parent], array[largest] = array[largest], array[parent]
        array = heapify(array, n, largest)

    return array

# ********************************************************************* #
# This file contains four sorting algorithms using the iterative method #
# ********************************************************************* #

# iterative merge sort implementaion
def mergeSort(array):

    # initial full array queue
    queue = [(0, len(array))]
    index = 0

    # generate queue of sub-array indexes
    while(True):
        left, right = queue[index]
        middle = (right + left) // 2
        index += 1

        if (right - left <= 1):
            break
        queue.append((left, middle))
        queue.append((middle, right))

    # run from LIFO queue to merge sub-arrays
    while(len(queue)):

        left, right = queue.pop(-1)
        middle = (right + left) // 2

        index = left
        left_array = array[left:middle]
        right_array = array[middle:right]

        while len(left_array) > 0 and len(right_array) > 0:
            if left_array[0] < right_array[0]:
                array[index] = left_array.pop(0)
            else:
                array[index] = right_array.pop(0)
            index += 1

        # add anything remaining in arrays
        while len(left_array) > 0:
            array[index] = left_array.pop(0)
            index += 1

        while len(right_array) > 0:
            array[index] = right_array.pop(0)
            index += 1

    return array


# iterative merge sort implementaion
def bubbleSort(array):

    for j in range(len(array)):
        swap_count = 0
        for i in range(len(array) - j - 1):
            if array[i] > array[i + 1]:
                array[i + 1], array[i] = array[i], array[i + 1]
                swap_count = 1

        # if iterate without swap, then sorted
        if swap_count == 0:
            break

    return array


# iterative quick sort implementaion
def quickSort(array):

    low = 0
    high = len(array) - 1
    queue = [(low, high)]

    while(len(queue)):

        low, high = queue.pop(0)

        if low < high:

            pivot = array[(low + high) // 2]
            i = low - 1
            j = high + 1

            for n in range(0, high - low):
                i += 1
                while(array[i] < pivot):
                    i += 1

                j -= 1
                while(array[j] > pivot):
                    j -= 1

                if i >= j:
                    break

                array[i], array[j] = array[j], array[i]

            queue.append((low, j))
            queue.append((j + 1, high))

    return array


# iterative heap sort implementaion
def heapSort(array):

    # heapify build max tree
    for i in range(len(array)//2 - 1, -1, -1):
        parent = i

        heapify(array, len(array), parent)

    # remove max value from heap array and rebuild max tree
    for i in range(len(array) - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        parent = 0

        heapify(array, i, parent)

    return array


# iterative heapify function
def heapify(array, n, parent):

    while(True):
        largest = parent
        left_child = 2 * parent + 1
        right_child = 2 * parent + 2

        # check if left child is greater than parent
        if left_child < n and array[left_child] > array[largest]:
            largest = left_child
        # check if right child is greater than parent
        if right_child < n and array[right_child] > array[largest]:
            largest = right_child

        if largest == parent:
            return

        array[parent], array[largest] = array[largest], array[parent]
        parent = largest

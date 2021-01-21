import time
import copy

import recursive_sort
import iterative_sort
import utility


# print(createList(100))

numbers = utility.createRandList(100)  # [7, 3, 9, 5, 6, 0, 1, 2, 4, 8]

# RUNNING RECURSIVE ALGORITHMS
lst = copy.deepcopy(numbers)
print(lst)

tic = time.perf_counter()
print(recursive_sort.mergeSort(lst))
toc = time.perf_counter()
print(f"mergeSort time: {toc - tic:0.7f}")


lst = copy.deepcopy(numbers)
print(lst)

tic = time.perf_counter()
print(recursive_sort.bubbleSort(lst, len(lst)))
toc = time.perf_counter()
print(f"bubbleSort time: {toc - tic:0.7f}")


lst = copy.deepcopy(numbers)
print(lst)

tic = time.perf_counter()
print(recursive_sort.quickSort(lst, 0, len(lst) - 1))
toc = time.perf_counter()
print(f"quickSort time: {toc - tic:0.7f}")


lst = copy.deepcopy(numbers)
print(lst)

tic = time.perf_counter()
print(recursive_sort.heapSort(lst))
toc = time.perf_counter()
print(f"heapSort time: {toc - tic:0.7f}")





# RUNNING ITERATIVE ALGORITHMS
lst = copy.deepcopy(numbers)
print(lst)

tic = time.perf_counter()
print(recursive_sort.mergeSort(numbers))
toc = time.perf_counter()
print(f"mergeSort time: {toc - tic:0.7f}")


lst = copy.deepcopy(numbers)
print(lst)

tic = time.perf_counter()
print(recursive_sort.bubbleSort(lst, len(lst)))
toc = time.perf_counter()
print(f"bubbleSort time: {toc - tic:0.7f}")


lst = copy.deepcopy(numbers)
print(lst)

tic = time.perf_counter()
print(recursive_sort.quickSort(lst, 0, len(lst) - 1))
toc = time.perf_counter()
print(f"quickSort time: {toc - tic:0.7f}")


lst = copy.deepcopy(numbers)
print(lst)

tic = time.perf_counter()
print(recursive_sort.heapSort(lst))
toc = time.perf_counter()
print(f"heapSort time: {toc - tic:0.7f}")

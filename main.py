import time
from sort import recursive_sort
from sort import iterative_sort
import utility
import gui

numbers = utility.createRandList(100)  # [7, 3, 9, 5, 6, 0, 1, 2, 4, 8]

# RUNNING RECURSIVE ALGORITHMS
lst = numbers[:]
tic = time.perf_counter()
recursive_sort.mergeSort(lst)
toc = time.perf_counter()
print(f"mergeSort time: {toc - tic:0.7f}")

lst = numbers[:]
tic = time.perf_counter()
recursive_sort.bubbleSort(lst, len(lst))
toc = time.perf_counter()
print(f"bubbleSort time: {toc - tic:0.7f}")

lst = numbers[:]
tic = time.perf_counter()
recursive_sort.quickSort(lst, 0, len(lst) - 1)
toc = time.perf_counter()
print(f"quickSort time: {toc - tic:0.7f}")

lst = numbers[:]
tic = time.perf_counter()
recursive_sort.heapSort(lst)
toc = time.perf_counter()
print(f"heapSort time: {toc - tic:0.7f}")


# RUNNING ITERATIVE ALGORITHMS
lst = numbers[:]
tic = time.perf_counter()
iterative_sort.mergeSort(lst)
toc = time.perf_counter()
print(f"mergeSort time: {toc - tic:0.7f}")

lst = numbers[:]
tic = time.perf_counter()
iterative_sort.bubbleSort(lst)
toc = time.perf_counter()
print(f"bubbleSort time: {toc - tic:0.7f}")

lst = numbers[:]
tic = time.perf_counter()
iterative_sort.quickSort(lst)
toc = time.perf_counter()
print(f"quickSort time: {toc - tic:0.7f}")

lst = numbers[:]
tic = time.perf_counter()
iterative_sort.heapSort(lst)
toc = time.perf_counter()
print(f"heapSort time: {toc - tic:0.7f}")


visual = gui.Visual_sorting_algorithms(numbers[:])
visual.run()

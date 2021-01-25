# ********************************************************************* #
# Test all recursive and iterative sorting algorithms with simple and   #
# random list of values.                                                #
# Usage: python -m unittest discover                                    #
# ********************************************************************* #

import unittest
import utility
from sort import recursive_sort
from sort import iterative_sort

NUMBERS = [7, 3, 9, 5, 6, 0, 1, 2, 4, 8]
NUMBERS_SORTED = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# Testing the recursive sorting algorithms
class TestRecursiveSort(unittest.TestCase):

    rand_numbers = utility.createRandList(100)

    # test merge sort with length 10
    def test_mergeSort(self):
        lst = cloning(NUMBERS)
        self.assertEqual(recursive_sort.mergeSort(lst), NUMBERS_SORTED)

    # test merge sort with random list length 100
    def test_rand_mergeSort(self):
        lst = cloning(self.rand_numbers)
        self.assertTrue(utility.is_sorted(recursive_sort.mergeSort(lst)))

    # test bubble sort with length 10
    def test_bubbleSort(self):
        lst = cloning(NUMBERS)
        self.assertEqual(recursive_sort.bubbleSort(lst, len(lst)), NUMBERS_SORTED)

    # test bubble sort with random list length 100
    def test_rand_bubbleSort(self):
        lst = cloning(self.rand_numbers)
        self.assertTrue(utility.is_sorted(recursive_sort.bubbleSort(lst, len(lst))))

    # test quick sort with length 10
    def test_quickSort(self):
        lst = cloning(NUMBERS)
        self.assertEqual(recursive_sort.quickSort(lst, 0, len(lst) - 1), NUMBERS_SORTED)

    # test quick sort with random list length 100
    def test_rand_quickSort(self):
        lst = cloning(self.rand_numbers)
        self.assertTrue(utility.is_sorted(recursive_sort.quickSort(lst, 0, len(lst) - 1)))

    # test heap sort with length 10
    def test_heapSort(self):
        lst = cloning(NUMBERS)
        self.assertEqual(recursive_sort.heapSort(lst), NUMBERS_SORTED)

    # test heap sort with random list length 100
    def test_rand_heapSort(self):
        lst = cloning(self.rand_numbers)
        self.assertTrue(utility.is_sorted(recursive_sort.heapSort(lst)))


# Testing the iterative sorting algorithms
class TestIterativeSort(unittest.TestCase):

    rand_numbers = utility.createRandList(100)

    # test merge sort with length 10
    def test_mergeSort(self):
        lst = cloning(NUMBERS)
        self.assertEqual(iterative_sort.mergeSort(lst), NUMBERS_SORTED)

    # test merge sort with random list length 100
    def test_rand_mergeSort(self):
        lst = cloning(self.rand_numbers)
        self.assertTrue(utility.is_sorted(iterative_sort.mergeSort(lst)))

    # test bubble sort with length 10
    def test_bubbleSort(self):
        lst = cloning(NUMBERS)
        self.assertEqual(iterative_sort.bubbleSort(lst), NUMBERS_SORTED)

    # test bubble sort with random list length 100
    def test_rand_bubbleSort(self):
        lst = cloning(self.rand_numbers)
        self.assertTrue(utility.is_sorted(iterative_sort.bubbleSort(lst)))

    # test quick sort with length 10
    def test_quickSort(self):
        lst = cloning(NUMBERS)
        self.assertEqual(iterative_sort.quickSort(lst), NUMBERS_SORTED)

    # test quick sort with random list length 100
    def test_rand_quickSort(self):
        lst = cloning(self.rand_numbers)
        self.assertTrue(utility.is_sorted(iterative_sort.quickSort(lst)))

    # test heap sort with length 10
    def test_heapSort(self):
        lst = cloning(NUMBERS)
        self.assertEqual(iterative_sort.heapSort(lst), NUMBERS_SORTED)

    # test heap sort with random list length 100
    def test_rand_heapSort(self):
        lst = cloning(self.rand_numbers)
        self.assertTrue(utility.is_sorted(iterative_sort.heapSort(lst)))


def cloning(lst):
    lst_copy = lst[:]
    return lst_copy


if __name__ == "__main__":
    unittest.main()

__author__ = 'Xidai'

import unittest
from src.xidai.xsort import xsort


class TestSort(unittest.TestCase):
    def test_insertion_sort(self):
        a = [1, 3, 2]
        sorted_a = xsort.insertion_sort(a)
        self.assertEqual(sorted_a, [1, 2, 3])

        b = [1, 1, 5, 6, 2, 2, 9]
        sorted_b = xsort.insertion_sort(b)
        self.assertEqual(sorted_b, [1, 1, 2, 2, 5, 6, 9])

        c = [3, 1, 2]
        sorted_c = xsort.insertion_sort(c)
        self.assertEqual(sorted_c, [1, 2, 3])

    def test_insertion_sort_descend(self):
        a = [1, 3, 2]
        sorted_a = xsort.insertion_sort_descend(a)
        self.assertEqual(sorted_a, [3, 2, 1])

        b = [1, 1, 5, 6, 2, 2, 9]
        sorted_b = xsort.insertion_sort_descend(b)
        self.assertEqual(sorted_b, [9, 6, 5, 2, 2, 1, 1])

        c = [3, 1, 2]
        sorted_c = xsort.insertion_sort_descend(c)
        self.assertEqual(sorted_c, [3, 2, 1])

    def test_merge_sort(self):
        a = [1, 3, 4, 2]
        sorted_a = xsort.merge_sort(a, 0, len(a) - 1)
        self.assertEqual(sorted_a, [1, 2, 3, 4])

        b = [1, 3, 2]
        sorted_b = xsort.merge_sort(b, 0, len(b) - 1)
        self.assertEqual(sorted_b, [1, 2, 3])

        c = [1, 1, 5, 6, 2, 2, 9]
        sorted_c = xsort.merge_sort(c, 0, len(c) - 1)
        self.assertEqual(sorted_c, [1, 1, 2, 2, 5, 6, 9])


if __name__ == "__main__":
    unittest.main()
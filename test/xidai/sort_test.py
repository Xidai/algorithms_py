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


if __name__ == "__main__":
    unittest.main()
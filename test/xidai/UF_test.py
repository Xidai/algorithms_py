__author__ = 'Xidai'


import unittest
from src.xidai import UF


class TestUF(unittest.TestCase):
    def test_quick_find(self):
        uf = UF.UF(10)
        uf.union(9, 5)
        uf.union(8, 7)
        uf.union(3, 9)
        uf.union(4, 8)
        uf.union(7, 0)
        uf.union(5, 1)

        self.assertEqual(uf.id, [0, 1, 2, 1, 0, 1, 6, 0, 0, 1])

    def test_weighted_quick_union(self):
        uf = UF.WeightedQuickUnionUF(10)
        uf.union(2, 1)
        uf.union(4, 1)
        uf.union(7, 9)
        uf.union(0, 4)
        uf.union(6, 5)
        uf.union(6, 7)
        uf.union(2, 3)
        uf.union(6, 0)
        uf.union(5, 8)

        self.assertEqual(uf.id, [0, 1, 2, 1, 0, 1, 6, 0, 0, 1])


if __name__ == "__main__":
    unittest.main()

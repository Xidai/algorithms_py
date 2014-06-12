__author__ = 'Xidai'
import sys


def insertion_sort(a):
    """
    For A[a1, a2, a3..., an], a1 <= a2 <= a3... <= an
    Sorted in place.
    O(n**2)
    """
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key

    return a


def insertion_sort_descend(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key > a[j]:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key

    return a


def merge_sort(a, p, r):
    """
    :param a: List needed to be sorted.
    :param p: Starting index.
    :param r: Ending index
    :return: Sorted list
    """

    if p < r:
        q = (p + r) / 2
        merge_sort(a, p, q)
        merge_sort(a, q + 1, r)
        merge(a, p, q, r)

    return a


def merge(a, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    left = []
    right = []
    for i in range(0, n1):
        left.append(a[p + i])
    for j in range(0, n2):
        right.append(a[q + 1 + j])
    right.append(sys.maxint)
    left.append(sys.maxint)

    i, j = 0, 0
    for k in range(p, r + 1):
        if left[i] <= right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1

    return a



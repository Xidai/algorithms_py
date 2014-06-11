__author__ = 'Xidai'


def insertion_sort(a):
    """
    For A[a1, a2, a3..., an], a1 <= a2 <= a3... <= an
    Sorted in place.
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

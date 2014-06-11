__author__ = 'Xidai'


def insertion_sort(a):
    """
    For A[a1, a2, a3..., an], a1 <= a2 <= a3... <= an
    Sorted in place.
    """
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        for j in range(i - 1, -1, -1):
            if key >= a[j]:
                break
            else:
                a[j + 1] = a[j]

        a[j + 1] = key

    return a

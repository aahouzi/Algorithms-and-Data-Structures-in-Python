############################################################################################
#                                  Author: Anas AHOUZI                                     #
#                               File Name: sorting_algos.py                                #
#                           Creation Date: August 31, 2020                                 #
#                         Source Language: Python                                          #
#     Repository: https://github.com/aahouzi/Algorithms-and-Data-Structures-in-Python      #
#                              --- Code Description ---                                    #
#                   Implementation of sorting algorithms in Python.                        #
############################################################################################


def selection_sort(A):
    """
    This algorithm starts by looking for the minimum's index in the list, and if it's different from
    the first element, it swaps the values, and then it repeats the same process recursively starting
    from the next element until the list is sorted. It has a time complexity of O(n²), and space
    complexity of O(1).
    :param A: A list.
    :return: A sorted list.
    """
    n = len(A)

    if n >= 2:
        if A.index(min(A)) != 0:
            j = A.index(min(A))
            A[0], A[j] = A[j], A[0]

        return [A[0]] + selection_sort(A[1:])

    else:
        return A


def bubble_sort(A):
    """
    This algorithm starts by comparing the next element to the previous one, and swaps them in case
    the first is smaller than the second. This process continues many times through all the list, and
    stops when there is no swaping when going through the list. It has a time complexity of O(n²),
    and space complexity of O(1).
    :param A: A list.
    :return: A sorted list.
    """

    n = len(A)
    while 1:
        count = 0
        for i in range(n-1):
            if A[i+1] < A[i]:
                A[i], A[i+1] = A[i+1], A[i]
                count += 1

        if count == 0:
            return A


def insertion_sort(A):
    """
    This algorithm will sort the list by comparing every time the i-th element with the
    previous ones, and then swaping when the i-th element is smaller. This process continues
    until the last element. It has a time complexity of O(n²), and space complexity of O(1).
    :param A: A list.
    :return: A sorted list.
    """
    n = len(A)

    for i in range(1, n):
        for k in range(i):
            if A[i] < A[k]:
                A[i], A[k] = A[k], A[i]

    return A


def counting_sort(A):
    """
    This algorithm sorts a list of positive elements, given that the range of the elements in the list is known.
    It first creates an intermediate list where the indexes are the elements of the list to sort,
    and then computes the cumulative index of each element. This cumulative index will then help
    us determine the exact location of every element in the output sorted list. This algo has
    the advantage of reducing dramatically the time complexity to a linear one O(n+m), where n and
    m are respectively the length of the list, and its maximum value plus one. However, it has a space complexity
    of O(n+m) since it's using two intermediate lists during the process.
    :param A: A list.
    :return: A sorted list.
    """
    n = len(A)
    size = max(A)
    output = [0] * n
    count = [0] * (size+1)

    for i in range(n):
        count[A[i]] += 1

    for j in range(1, size+1):
        count[j] += count[j-1]

    for k in range(n):
        output[count[A[k]]-1] = A[k]
        count[A[k]] -= 1

    return output


def merge(left, right):
    """
    This function is used in the merging sort algorithm to merge with the correct order two lists.
    :param left: The left list.
    :param right: The right list.
    :return: A merged and sorted list.
    """

    L = []
    while len(left) != 0 and len(right) != 0:
        if left[0] <= right[0]:
            L.append(left.pop(0))
        else:
            L.append(right.pop(0))

    if len(left) == 0:
        return L + right
    elif len(right) == 0:
        return L + left


def merge_sort(A):
    """
    This algorithm sorts a list by using the method "Divide And Conquer", and it breaks the problem into simpler sub
    problems. It starts by sorting the smaller sub-lists, and then merging them together step by step until it
    reconstructs the original list in a sorted order. It has a time complexity of O(nlog(n)), and a space complexity
    of O(n).
    :param A: A list.
    :return: A sorted list.
    """
    n = len(A)
    m = n // 2

    if n >= 2:
        left = merge_sort(A[0:m])
        right = merge_sort(A[m:])
        out = merge(left, right)
        return out
    else:
        return A, 0


def partition(A, l, h):
    """
    This function is the key for quicksort, since it picks the last element of a list as a pivot, and finds
    its exact location in the list where all smaller elements are before the pivot and greater elements are
    after it.
    :param A: A list.
    :param l: Lower bound starting index.
    :param h: Higher bound finishing index.
    :return: The pivot index.
    """

    # The last element is picked as pivot
    pivot = A[h]
    # We take l-1 in case the first element is lower than pivot, so it's swaped with himself
    # since we don't know if the next number is greater or lower.
    k = l - 1

    for i in range(l, h):

        if A[i] < pivot:
            k += 1
            A[i], A[k] = A[k], A[i]

    A[k+1], A[h] = A[h], A[k+1]

    return k+1


def quicksort(A, l, h):
    """
    This algorithm sorts a list by selecting a pivot, and putting it in a position where all smaller elements are before,
    and greater elements are after. Then, it continues doing the same process for the left and right sides of the pivot
    until the list is sorted. It has a time complexity of O(nlogn), and a space complexity of O(logn).
    :param A: An unsorted list.
    :param l: Lower bound starting index.
    :param h: Higher bound finishing index.
    :return:
    """

    if l < h:
        pi = partition(A, l, h)
        quicksort(A, l, pi-1)
        quicksort(A, pi+1, h)





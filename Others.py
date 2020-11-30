############################################################################################
#                                  Author: Anas AHOUZI                                     #
#                               File Name: Others.py                                       #
#                           Creation Date: August 31, 2020                                 #
#                         Source Language: Python                                          #
#     Repository: https://github.com/aahouzi/Algorithms-and-Data-Structures-in-Python      #
#                              --- Code Description ---                                    #
#                      Implementation of other utility functions.                          #
############################################################################################


def list_intersect(a, b):
    """
    This function uses hashmaps data structure (dictionnaries in Python), to reduce the complexity
    of finding the intersection between two lists from O(m*n) to O(m+n).
    :param a: The first list of size n.
    :param b: The second list of size m.
    :return: A list containing the intersection between a and b.
    """
    empty_dict = dict()
    for l in a:
        empty_dict[l] = True

    inter = []
    for m in b:
        if m in empty_dict.keys():
            inter.append(m)

    return inter


def min_coins(amount, c):
    """
    This problem is a simple illustration of a Dynamic Programming problem. Given a list of available coins and
    a certain amount of money, we are asked to figure out the minimum number of coins that sum up to that amount.
    :param amount: An amount of money.
    :param c: A list containing available change or coins.
    :return:
    """

    L = [0] + [10000 for _ in range(amount)]
    for coin in c:
        for i in range(1, amount + 1):
            if i >= coin:
                L[i] = min(L[i], L[i - coin] + 1)

    return -1 if L[amount] > amount else L[amount]




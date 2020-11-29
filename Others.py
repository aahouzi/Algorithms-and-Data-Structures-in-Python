
# This function uses hash tables concept represented by dicts in Python,
# to reduce complexity from O(m*n) to O(m+n).


def list_intersect(a, b):
    empty_dict = dict()
    for l in a:
        empty_dict[l] = True

    inter = []
    for m in b:
        if m in empty_dict.keys():
            inter.append(m)

    return inter



def get_digits(n):
    l = []

    while n != 0:
        l.append(n % 10)
        n = n // 10

    return l[::-1]


def k_smallest(arr, k):
    n = len(arr)
    new_arr = sorted(arr)

    s = 1
    i = 1
    elt = new_arr[0]
    while s < k and i < n:
        if elt != new_arr[i]:
            s += 1
            elt = new_arr[i]
        i += 1

    if s == k:
        return elt
    else:
        return "NULL"


def test(s):

    n = len(s)

    copy = ''.join(list(s))
    i = 1
    k = 0
    while i < n:
        if int(s[0:i]) % 2 == 0 and int(s[i]) % 2 == 0:
            copy = copy[0:i+k] + '*' + copy[i+k:]
            k += 1
        elif int(s[0:i]) % 2 != 0 and int(s[i]) % 2 != 0:
            copy = copy[0:i+k] + '-' + copy[i+k:]
            k += 1

        i += 1

    return copy


def check_palindrome(n):

    chiff = []
    l = []

    for s in str(n):
        chiff.append(s)

    while len(chiff) > 0:
        l.append(chiff.pop())

    if ''.join(l) == str(n):
        return 1
    else:
        return 0


def func(n):

    reverse = str(n)[::-1]
    num_iter = 0
    m = int(reverse) + n

    while num_iter < 1000 and m < 4294967295:
        if check_palindrome(m):
            return m
        else:
            m += int(str(m)[::-1])

        num_iter += 1

    return "No palindrom exists"



def spiral_form(mat):

    l = len(mat)
    c = len(mat[0])

    final_arr = []
    k = 0
    while l >= 3:
        arr = mat[0] + [mat[i][c-1] for i in range(1, l)] + mat[l-1][0:c-1][::-1] + [mat[l-1-i][0] for i in range(1, l-1)]
        final_arr += arr
        mat = mat[1:l-1]
        for i in range(len(mat)):
            mat[i] = mat[i][1:c-1]

        l -= 2
        c -= 2

    if len(mat) == 2:
        final_arr += mat[0] + mat[1][::-1]

    elif len(mat) == 1:
        final_arr += mat[0]

    for i in range(len(final_arr)):
        print(final_arr[i])


def survivor(n, k):

    l = [i for i in range(n)]

    m = k-1
    while len(l) != 1:
        l.pop(m)
        m = ((m + k - 1) % len(l))

    return l[0]+1


def swap_str(s, i, j):

    l = [elt for elt in s]
    l[i], l[j] = l[j], l[i]

    return ''.join(l)


def checker(tmp):
    check = {}
    for e in tmp:
        if e not in check:
            check[e] = 1
        else:
            return False

    return True


def find_scroll(A, B):

    for k in range(A, B+1):
        tmp = get_digits(k)

        if checker(tmp):
            L = []
            m = len(tmp)
            t = 0
            while len(L) < m:
                t = (t+tmp[t]) % m
                if t in L:
                    break
                else:
                    L.append(t)

            if len(L) == m:
                print(k)



def min_coins(amount, c):

    L = [0] + [10000 for _ in range(amount)]
    for coin in c:
        for i in range(1, amount + 1):
            if i >= coin:
                L[i] = min(L[i], L[i - coin] + 1)

    return -1 if L[amount] > amount else L[amount]


adjecendy_mat = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
                 [4, 0, 8, 0, 0, 0, 0, 11, 0],
                 [0, 8, 0, 7, 0, 4, 0, 0, 2],
                 [0, 0, 7, 0, 9, 14, 0, 0, 0],
                 [0, 0, 0, 9, 0, 10, 0, 0, 0],
                 [0, 0, 4, 14, 10, 0, 2, 0, 0],
                 [0, 0, 0, 0, 0, 2, 0, 1, 6],
                 [8, 11, 0, 0, 0, 0, 1, 0, 7],
                 [0, 0, 2, 0, 0, 0, 6, 7, 0]]
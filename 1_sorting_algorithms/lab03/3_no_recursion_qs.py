from collections import deque


def quick_sort(A: list):
    n = len(A)
    stack = [(0, n - 1)]
    while len(stack) != 0:
        a, b = stack.pop()
        if a < b:
            s = partition(A, a, b)
            stack.append((a, s - 1))
            stack.append((s + 1, b))
    print(A)


def partition(A: list, left, right):
    l = left
    r = right - 1
    pivot = right
    while l < r:
        while A[l] <= A[pivot] and l < r:
            l += 1
        while A[r] > A[pivot] and l < r:
            r -= 1
        A[l], A[r] = A[r], A[l]
    if A[l] > A[pivot]:
        middle = l
    else:
        middle = l + 1
    A[middle], A[pivot] = A[pivot], A[middle]
    return middle


quick_sort([6, 12, 7, 3, 8, 1, 2])

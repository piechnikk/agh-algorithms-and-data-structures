# Hoare partition algorithm
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

# insertion sort
def insertion_sort(A):
    l = len(A)
    for i in range(l):
        for j in range(i, 0):
            if A[j - 1] < A[j]:
                A[j - 1], A[j] = A[j], A[j - 1]

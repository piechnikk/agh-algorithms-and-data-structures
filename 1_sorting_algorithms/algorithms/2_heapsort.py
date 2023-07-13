# firstly i build a heap  by calling the heapify function (that fixes a heap where one element is in the wrong place) n-1 times from the back of the table, setting the array innto a heap, which is finally sorted
# complexity O(nlogn)

def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

def parent(i):
    return (i - 1) // 2

def heapify(A, n, i):
    max_i = i
    l = left(i)
    r = right(i)

    if l < n and A[l] > A[max_i]:
        max_i = l

    if r < n and A[r] > A[max_i]:
        max_i = r

    if max_i != i:
        A[i], A[max_i] = A[max_i], A[i]
        heapify(A, n, max_i)

def buildheap(A):
    n = len(A)
    for i in range(parent(n - 1), -1, -1):
        heapify(A, n, i)

def sort(A):
    n = len(A)
    buildheap(A)
    for i in range(n - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapify(A, i, 0)

A = [1, 4, 6, 2, 5, 23, 4, 234, 2, 5, 43, 6, 37, 6, 73, 24, 62, 5, 1]
sort(A)
print(A)

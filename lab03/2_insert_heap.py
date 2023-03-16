# insert heap
def parent(i):
    return (i - 1) // 2


def heapify(A: list, i):
    p = parent(i)
    if i != 0 and A[i] > A[p]:
        A[i], A[p] = A[p], A[i]
        heapify(A, p)


def insert(A: list, el):
    n = len(A)
    A.append(el)
    heapify(A, n)


heap = [13, 9, 8, 7]
insert(heap, 15)
print(heap)

# quick sort with O(logn) memory complexity
def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def quick_sort(A, p, r):
    if p<r:
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)

A = [1, 4, 6, 2, 5, 23, 4, 234, 2, 5, 43, 6, 37, 6, 73, 24, 62, 5, 1]
quick_sort(A, 0, len(A)-1)
print(A)

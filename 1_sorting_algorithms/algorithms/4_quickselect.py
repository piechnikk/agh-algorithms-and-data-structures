# I choose the last element to pivot, and do a partition, if q==k then it is the element I am looking for, if q>k, I search in the first half, else in the second half 
# complexity is O(n)
def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def quick_select(A, k):
    n = len(A)
    p = 0
    r = n - 1
    q = partition(A, p, r)
    while True:
        if q == k:
            return A[k]
        elif q > k:
            r = q - 1
        else:
            p = q + 1
        q = partition(A, p, r)

A = [1, 4, 6, 2, 5, 23, 4, 234, 2, 5, 43, 6, 37, 6, 73, 24, 62, 5, 1]

print(quick_select(A, 4))
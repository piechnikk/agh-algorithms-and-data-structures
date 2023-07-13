# array C (k elements), to B (n elements) it will rewrites the result, to C it write the number of occurrences of this element and then wwe write  out one by one
# complexity is O(n+k)
def sort(A, k):
    n = len(A)
    C = [0] * k
    B = [0] * n
    for i in range(n):
        C[A[i]] += 1
    for i in range(1, k):
        C[i] += C[i - 1]
    for i in range(n - 1, -1, -1):
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]
    for i in range(n):
        A[i] = B[i]


A = [0, 1, 0, 1, 0, 3, 0, 3, 3, 1]
sort(A, 4)
print(A)

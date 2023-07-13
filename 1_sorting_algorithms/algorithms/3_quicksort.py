# takes the last element from the table as a pivot and goes through the table pre-sorting the table  so that after the partition, pivot is in his place, before it there are elements amaller than it and after it elements larger than it and runs quicksort first for elementts before and then for elements after
# complexity us O(nlogn), in the worst case O(n^2) - whe they split into one element and the rest of the array
def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def quick_sort(A, p, r):
    # if p < r:
    #     q = partition(A, p, r)
    #     quick_sort(A, p, q - 1)
    #     quick_sort(A, q + 1, r)
    # usunięcie rekurencji ogonowej
    while p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        p = q + 1

A = [1, 4, 6, 2, 5, 23, 4, 234, 2, 5, 43, 6, 37, 6, 73, 24, 62, 5, 1]
quick_sort(A, 0, len(A) - 1)
print(A)
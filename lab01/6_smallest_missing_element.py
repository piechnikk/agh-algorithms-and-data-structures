# As input, we have a sorted sequence of integers A={a0,...,an-1} in the range from 0 to m-1. The numbers are pairwise different. Moreover, n<m. Please give an algorithm that finds the smallest integer not in A.
def smallest(A):
    n = len(A)
    start = 0
    end = n
    while start != end:
        middle = start + (end - start) // 2
        if middle < A[middle]:
            end = middle
        else:
            start = middle + 1
    return start


print(smallest([0, 1, 2, 3, 4, 5, 6, 7, 9, 12]))

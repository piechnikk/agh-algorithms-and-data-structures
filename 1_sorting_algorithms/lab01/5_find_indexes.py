# find 2 indexes (i,j) such that T[i]-T[j]=6
def find_indexes(A):
    j, i = 0, 1
    while i < len(A) and A[i] - A[j] != 6:
        if A[i] - A[j] < 6:
            i += 1
        else:
            j += 1
    return i, j

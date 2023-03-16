# Check if 2 indexes (i,j) such that T[i] + T[j] = x exists
def find_indexes2(A, x):
    i, j = 0, len(A) - 1
    while i != j or A[j] + A[i] != x:
        if A[i] + A[j] > x:
            j -= 1
        elif A[i] + A[j] < x:
            i += 1
        else:
            return True
    return False

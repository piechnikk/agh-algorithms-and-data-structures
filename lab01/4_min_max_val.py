# find min and max value from a list with n elements using only (3/2)*n comparisons
def find_min_max(A: list):
    min_val = max_val = A[0]
    for i in range(0, len(A), 2):
        if A[i] < A[i + 1]:
            if A[i] < min_val:
                min_val = A[i]
            if A[i + 1] > max_val:
                max_val = A[i + 1]
        else:
            if A[i + 1] < min_val:
                min_val = A[i + 1]
            if A[i] > max_val:
                max_val = A[i]

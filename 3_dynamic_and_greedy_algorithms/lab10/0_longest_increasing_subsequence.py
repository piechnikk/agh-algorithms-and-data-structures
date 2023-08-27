# we are looking for the length of the longest (not necessarily consistent) subsequence from the array of numbers "A"

def lisReq(A):
    n = len(A)
    F = [None] * n  # array with results
    F[0] = 1

    def req(i):
        if F[i]:
            return F[i]
        
        max_len = 0
        for j in range(i):
            if A[j]<A[i]:
                temp_len = req(j)
                if temp_len > max_len:
                    max_len = temp_len

        F[i] = max_len + 1
        return F[i]
    
    for i in range(n-1, 0, -1):
        if not F[i]:
            req(i)

    return max(F)

def lis(A):
    # this gives length of the searched subsequence
    n = len(A)
    F = [1] * n  # array with results
    parents = [-1] * n
    for i in range (1, n):
        for j in range(i):
            if A[j] < A[i] and F[j] + 1 > F[i]:
                parents[i] = j
                F[i] = F[j] + 1
    len_lis = max(F)

    # this returns the searched subsequence
    subsequence = []
    x = F.index(len_lis)
    subsequence.append(A[x])
    while parents[x]!=-1:
        x = parents[x]
        subsequence.append(A[x])
        

    return len_lis, subsequence


A = [2, 1, 4, 3, 1, 5, 2, 7, 8, 3]
print(lisReq(A))
print(lis(A))


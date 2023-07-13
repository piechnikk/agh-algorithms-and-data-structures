# sorts recursively left half of the data, sort recursively right half of the data, merge sorted halves
# complexity T(n) = cnlogn

def mergesort(A):
    n = len(A)
    if n > 1:
        L = A[:n//2]
        R = A[n//2:]
        mergesort(L)
        mergesort(R)

        i = il = ir = 0
        while il < len(L) or ir < len(R):
            if il == len(L):
                A[i] = R[ir]
                ir+=1
            elif ir == len(R):
                A[i] = L[il]
                il+=1
            elif L[il] <= R[ir]:
                A[i] = L[il]
                il+=1
            else:
                A[i] = R[ir]
                ir+=1
            i+=1

x = [1,2,3,5,1,8,9,3,24]
mergesort(x)
print(x)
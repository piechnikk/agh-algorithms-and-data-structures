from egz2atesty import runtests

def coal( A, T ):
    n = len(A)
    storages = []
    for i in range(n):
        storage = -1
        for j in range(len(storages)):
            if A[i] <= storages[j]:
                storage = j
                break
        if storage == -1:
            storage = len(storages)
            storages.append(T)
        
        storages[storage] -= A[i]

    return storage

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( coal, all_tests = True )

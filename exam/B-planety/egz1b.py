# Paweł Piechnik
# tworzę sobie tablice kosztów w której przechowuje ile kosztowało dostanie się do planety i z b tonami paliwa (costs[i][b]) dla każdej planety obliczam uzupełniam tę tablicę min(wartość która już się tam znajduje(bo po ustawieniu costs[i] zapisuje na planecie T[i] koszt po przeteleportowaniu się), sytuacja jak doleciałem z pustym bakiem i tankuje b litrów, sytuacja gdy doleciałem z jakimś paliwem w baku) złożoność to  O(nE)
from egz1btesty import runtests
inf = float("inf")
def planets( D, C, T, E ):
    n = len(D)
    costs = [[inf for _ in range(E+1)] for _ in range(n)]

    # uzupełaniam tablice z wynikami dla planety A
    for b in range(E+1):
        costs[0][b] = C[0] * b
    # teleport
    if T[0][0] != 0:
        costs[T[0][0]][0] = T[0][1]

    # uzupełniam tablice z wynikami dla reszty planet
    for i in range(1,n):
        for b in range(E+1):
            costs[i][b] = min(
                costs[i][b], 
                costs[i-1][D[i]-D[i-1]] + C[i] * b, 
                costs[i-1][D[i]-D[i-1]+b] if D[i]-D[i-1]+b < E+1 else costs[i-1][E] + C[i]*(D[i]-D[i-1]+b-E)
            )
        # teleport
        if T[i][0] != i:
            costs[T[i][0]][0] = min(costs[T[i][0]][0], costs[i][0]+T[i][1])
            # print(costs[T[i][0]][0], T[i][0], i)
    # for i in range(n):
    #     print(costs[i])
    
    return costs[n-1][0]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = True )

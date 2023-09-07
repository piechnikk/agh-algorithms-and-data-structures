# Paweł Piechnik
# Dla każdego punktu sprawdzam ile punktów dominuje, zwracam największą wartość. Złożoność O(n^2)
from egz2atesty import runtests

def dominance(P):
    n = len(P)
    max_points = 0
    for i in range(n):
        temp = 0
        for j in range(n):
            if P[j][0] < P[i][0] and P[j][1] < P[i][1]:
                temp += 1
        max_points = max(max_points, temp)

    return max_points
  
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )

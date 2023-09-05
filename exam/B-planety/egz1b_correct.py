from egz1btesty import runtests
inf = float("inf")

# f(i, b) = minimum cost to get to planet i with b fuel
# f(i, b) = 
def planets( D, C, T, E ):
    n = len(D)
    answers = [[inf] * (E + 1) for _ in range(n)]
    
    # answers for start planet
    for b in range(E + 1):
        answers[0][b] = b * C[0]
    if T[0][0] != 0: # teleport
        answers[T[0][0]][0] = min(answers[T[0][0]][0], answers[0][0] + T[0][1])
    
    for i in range(1, n):
        for b in range(E + 1):
            distance = D[i] - D[i - 1]
            possible_costs = [answers[i][b]] # teleport
            if b + distance <= E:
                possible_costs.append(answers[i - 1][b + distance]) # without refueling
                for j in range(b + distance + 1):
                    possible_costs.append(answers[i - 1][b + distance - j] + j * C[i - 1]) # with refueling j fuel

            answers[i][b] = min(possible_costs)
        if T[i][0] != i: # teleport from i to T[i][0] planet
            answers[T[i][0]][0] = min(answers[T[i][0]][0], answers[i][0] + T[i][1])
        
    return min(answers[n-1])
        
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = True )

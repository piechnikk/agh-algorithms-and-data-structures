def full_tanking(S, b, l):
    S.append((b, 0))
    cost = [float('inf') for _ in range(len(S))]
    cost[0] = S[0][1] * l

    for i in range(len(S)):
        j = i+1

        while j < len(S) and S[j][0] <= S[i][0] + l:
            cost[j] = min(cost[j], cost[i] + (S[j][0] - S[i][0]) * S[j][1])
            j+=1
    return cost
S = [(0, 1), (6, 3), (7, 5), (14, 6)]
print(full_tanking(S, 20, 7))
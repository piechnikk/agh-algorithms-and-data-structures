# an array is given with the distance of the station from 0 and the price of fuel at the station S = [(distance, price), ...]
# tank capacity = T
# you have to get to station n-1 at the lowest cost
# you have to always fill up to a full tank

def full_tanking(S, T): # S[i][0 -> distance, 1 -> price]
    n = len(S)
    cost = S[0][1] * T
    position = 0 # actual position
    while position+T < S[n-1][0]:
        best = min(list(filter((lambda x: (x[0]>position and x[0]<=position+T)), S)), key=lambda x: x[1])
        cost += (best[0]-position) * best[1]
        position = best[0]
    return cost
S = [(0, 1), (6, 3), (7, 5), (14, 6), (20, 0)]
print(full_tanking(S,7))

def hungry_frog(T):
    ln = len(T)
    to_end = [float('inf') for _ in range(ln)]
    to_end[ln -1] = 0
    
    for i in range (ln-2, -1, -1):
        for j in range(T[i], 0, -1):
            if i+j < ln  and  to_end[i+j] + 1 < to_end[i]:
                to_end[i] = to_end[i+j] +1

    return to_end[0]



DP = dict()

def frog(i, energy, C):
    global DP
    # print(i, energy, energy + i, len(C))
    if energy + i >= len(C):
        return 1
    if i >= len(C):
        return float("inf")
    key = (i, energy) 
    if key in DP:
        return DP[key]
    jumps = [frog(i + x, energy - x + C[i + x], C) for x in range(1, min(energy - i, len(C) - i - 1))]
    if len(jumps) == 0:
        jumps = [float("inf")]
    lowest_jumps = min(jumps)
    DP[key] = lowest_jumps + 1
    return lowest_jumps + 1

lilypads = [5, 5, 0, 0, 0, 0, 0, 0, 0, 0]

print(frog(0, lilypads[0], lilypads))

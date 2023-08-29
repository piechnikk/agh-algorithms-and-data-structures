def hungry_frog(T):
    n = len(T)
    passed_snacks = []
    energy = T[0]
    answer = 1
    for i in range(1,n-1):
        # when it is not possible to reach the end
        if energy == 0:
            return float("inf")

        # cost of moving one field
        energy -= 1

        # when there is any snack in the field add it to the passed_snacks array
        if T[i]>0:
            passed_snacks.append(T[i])
        
        # when there is no energy in our frog give it the largest passed snack and save how many snacks it ate
        if energy == 0:
            passed_snacks.sort()
            energy += passed_snacks.pop()
            answer+=1
        
    return answer



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
print(hungry_frog(lilypads))

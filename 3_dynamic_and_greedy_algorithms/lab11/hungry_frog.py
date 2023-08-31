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

# cost of jump is length^2
# f(i, a) = minimal jumps to i field with a energy after
# f(0, a) = 0
# f(i, a) = min(f(j,a-(i-j)+T[j])+1 for j in range(i))
def hungry_frog_square(T):
    n = len(T)
    sumA = sum(T)
    answers = [[float("inf")] * (sumA+1) for i in range(n)]
    for j in range(T[0]+1):
        answers[0][j] = 0
    for i in range(1,n):
        for a in range(sumA):
            answers[i][a] = min(answers[j][a+(i-j)**2-T[j]]+1 if a+(i-j)**2-T[j] >= 0 and a+(i-j)**2-T[j] <=sumA else float("inf") for j in range(i))
    return min(answers[n-1])


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
print(hungry_frog_square([1,5,1,3]))
print(hungry_frog_square_recursive([1,5,1,3]))

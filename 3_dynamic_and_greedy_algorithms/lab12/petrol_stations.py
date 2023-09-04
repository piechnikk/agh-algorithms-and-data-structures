# The tractor goes from point A to point B. 
# The tractor's consumption is exactly one litre of fuel per kilometre. 
# There is exactly L litres of fuel in the tank. 
# The route from A to B is a straight line with petrol stations 
# (at positions that are natural numbers; A is at position 0; B is at position n-1).
# Please provide an algorithm for the following cases:

# a. we choose the stations at which we refuel so that the number of refuellings is minimal
def minimum_refuelings(S, L):
    n = len(S)
    refuelings = 1
    position = S[0]
    for i in range(n-1):
        if S[i+1] > position+L:
            position = S[i]
            refuelings+=1
    return refuelings

print(minimum_refuelings([0, 5, 15, 20, 25, 26], 10))

# b. we choose the stations so that the cost of the journey is minimal (in this case, each station has a price per litre of fuel). 
#    We can fill up as much fuel as we like at each station
def optimum_refuelings(S, L):
    n = len(S)
    i = 0
    fuel = 0
    cost = 0
    cheaper_station = 0
    while i < n-1:
        # find a cheaper station than the current one
        cheaper_station = S[i]
        for j in range(i+1, n-1):
            if S[j][1] < cheaper_station[1] :
                cheaper_station = S[j]
                break
            if S[j+1][0] > S[i][0] + L:
                break
        
        # if you are at the cheaper station it means it is the cheapest station in the range so fill up to a full tank
        # else fill up enough to get to a cheaper station
        if S[i][0] == cheaper_station[0]:
            to_refuel = min(L - fuel, S[n-1][0] - S[i][0])
        else:
            distance = cheaper_station[0] - S[i][0]
            to_refuel = max(0, distance - fuel)

        fuel += to_refuel
        cost += to_refuel * S[i][1]

        # go to next station
        fuel -= S[i+1][0] - S[i][0]
        i+=1
    return cost

print(optimum_refuelings([(0, 3), (2, 2), (5, 4), (6, 10), (7, 2), (8, 1), (10, 3)], 4))

# c. we choose the stations so that the cost of the journey is minimal (in this case, each station has a price per litre of fuel). 
#    If we fill up at a station then we have to fill up the whole tank.
# f(i, t) = cost from 0 to i, ending with t fuel
def full_optimum_refuelings(S, L):
    n = len(S)
    answers = [[float("inf")] * (L + 1) for i in range(n)]
    answers[0][L] = S[0][1] * L
    for i in range(1, n):
        for j in range(i):
            distance = S[i][0]-S[j][0]
            if distance <= L:
                answers[i][L-distance] = answers[j][L]
        fuel, cost = min(enumerate(answers[i]), key=lambda x: x[1] + S[i][1] * (L-x[0]))
        answers[i][L] = cost + S[i][1] * (L-fuel)
    return min(answers[n-1])

print(full_optimum_refuelings([(0, 3), (2, 2), (5, 4), (6, 10), (7, 2), (8, 1), (10, 3)], 4))
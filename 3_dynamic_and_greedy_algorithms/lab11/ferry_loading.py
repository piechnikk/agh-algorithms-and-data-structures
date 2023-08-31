# we have 2 decks of length L and an array C with the length of the cars
# how many cars at the most can enter the ferry
# f(i, t, b) = maximum number of cars from subset from 0 to i from an array C that can fit on the ferry with top deck with length t and bottom deck with length b
# f(i, t, b) = max(put car on top deck, put car on bottom deck, don't take this car)
# f(i, t, b) = max(f(i-1, t-C[i], b), f(i-1, t, b-C[i]), f(i-1, t, b)) 
def ferry(C, L):
    n = len(C)
    answers = [[[None] * (L+1) for t in range(L+1)] for i in range(n)]

    def f(i, t, b):
        if t < 0 or b < 0:
            return 0
        if answers[i][t][b] != None:
            return answers[i][t][b]
        if i==0:
            answers[i][t][b] = 0
            if C[i] <= t or C[i] <= b:
                answers[i][t][b] = 1
            return answers[i][t][b]
        answers[i][t][b] = max(f(i-1, t-C[i], b)+1 , f(i-1, t, b-C[i])+1, f(i-1, t, b))
        return answers[i][t][b]
    
    return f(n-1, L, L)
            
print(ferry([1,1,1,2,3,4,5,6,7], 5))
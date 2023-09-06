from egz2btesty import runtests
inf = float("inf")

def magic( C ):
    n = len(C)
    answers = [0] * (n+1)
    answers[0] = C[0][0]
    for i in range(n):
        if answers[i] == 0: # there is no path to this chamber
            continue
        if i!=0: # exception for chamber 0
            answers[i] = answers[i]+C[i][0]
        for j in range(1,4): 
            if C[i][0] - C[i][j][0] <= 10: # you can take enough gold to leave the required amount
                answers[C[i][j][1]] = max(answers[C[i][j][1]], answers[i] - C[i][j][0]) # maximum amount of gold after comming from chamber 0
    if answers[n-1] != 0: # if there is path to chamber n-1
        return answers[n-1] - C[n-1][0]
    return -1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( magic, all_tests = True )

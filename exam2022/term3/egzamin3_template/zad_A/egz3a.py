from egz3atesty import runtests

def snow( T, I ):
    n = len(I)
    answers = [0] * T
    for i in range(n):
        for j in range(I[i][0], I[i][1]+1):
            answers[j]+=1
    return max(answers)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )

from egz1atesty import runtests

def snow(S:list):
    n = len(S)
    S.sort(reverse=True)
    snow = 0
    for i in range(n):
        if i >= S[i]:
            break
        snow += S[i] - i
    return snow

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = False )

# Paweł Piechnik
# W komórkach tablicy answers zapisuje sobie wyniki funkcji rekurencyjnej f(i, j), 
# ta funkcja dodaje odległość od budynku X[i] do działki Y[j] do najmniejszej sumy odległości budynków (od X[0] do X[i-1]) do parkingów (od Y[0] do Y[j-1]). 
# Zwracam najmniejszą odległość dla n-1 budynków. Złożoność to O(mn)

# f(i, j) = minimalna suma odległości biurowców z pozycji od 0 do i do przydzielonych działek, biurowiec X[i] ma przydzieloną działkę Y[j]
# f(0, j) = abs(X[0] - Y[j])
# f(i, j) = abs(X[i] - Y[j]) + min(f(i-1, k) for k in range(j))



from egz2btesty import runtests

def parking(X,Y):
    n = len(X)
    m = len(Y)
    answers = [[float("inf")] * m for _ in range(n)]
    for j in range(m):
        answers[0][j] = abs(X[0] - Y[j])
    for i in range(1, n):
        for j in range(i, m):
            answers[i][j] = abs(X[i] - Y[j]) + min(answers[i - 1][:j])
    return min(answers[n-1])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( parking, all_tests = True )

# szachownica o wymiarach n x n
# figura stoi w lewym gornym rogu
# moze poruszac sie tylko jedno pole w dol lub jedno pole w prawo
# chcemy dostac sie do prawego dolnego rogu
# kazde pole ma koszt zatrzymania sie na nim
# jaka droge obrac aby jak najmniejszym kosztem przedostac sie do prawego dolnego rogu?

# funkcja definiujaca rozwiazanie:
# funkcja f(x, y) -> |N, x oraz y to obecne koordynaty figury, zwraca minimalny koszt dojscia z punktu (x, y) do (n, n)
# f(n, n) = 0
# f(x, y) = min(
#               C[x + 1][y] + f(x + 1, y),
#               C[x][y + 1] + f(x, y + 1)
#           )
# f(x, y) = inf gdy x > n lub y > n


def path(C):
    n = len(C)
    costs = [[float("inf") * n] for _ in range(n)]
    costs[n - 1][n - 1] = 0
    for x in range(n - 1, 0, -1):
        for y in range(n - 1, 0, -1):
            if x == -1 and y == -1:
                continue
            # zadbac o liczenie na brzegach!!!
            costs[x - 1][y - 1] = min(costs[x + 1][y] + C[x + 1][y], costs[x][y + 1] + C[x][y + 1])
    return costs[0][0]
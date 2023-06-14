# Bartosz Sajecki

# korzystajac z funkcji:
# f(x, y), ktora zwraca maksymalna liczbe komnat odwiedzonych od rogu [0, 0]
# do komnaty o koordynatach [x, y], mozna obliczyc wartosci dla calej macierzy
# a nastepnie zwrocic f(n - 1, n - 1)

# dir - kierunek z ktorego przyszlismy (2 - z gory, 1 - z lewej, 0 - z dolu)
# f(x, y, dir) = {
#               -infinity, gdy L[x][y] == "#" lub y > n - 1 lub x > n - 1
#               1, gdy x = y = n - 1
#               max(f(x, y - 1, 0), f(x + 1, y, 2)) + 1, gdy dir = 0
#               max(f(x, y - 1, 0), f(x, y + 1, 0), f(x + 1, y, 2)) + 1, gdy dir = 1
#               max(f(x, y + 1, 2), f(x + 1, y, 1)) + 1, gdy dir = 2
#           }


from zad7testy import runtests


def maze( L ):
    # tu prosze wpisac wlasna implementacje
    n = len(L)
    neg_inf = -float("inf")
    output = [[[None] * 3 for _ in range(n)] for _ in range(n)]
    output[n - 1][n - 1] = [0, 0, 0]
    def max_distance(x, y, dir, depth):
        # print("depth of", depth)
        if not (0 <= x < n and 0 <= y < n) or L[y][x] == "#":
            return neg_inf
        # if depth > 1955: print("depth of", depth, "x", x, "y", y, "char", L[y][x], "distance", output[y][x])
        value = output[y][x][dir]
        if value is not None:
            return value
        if dir == 0:
            value = max(max_distance(x, y - 1, 0, depth + 1), max_distance(x + 1, y, 1, depth + 1)) + 1
        if dir == 1:
            value = max(max_distance(x, y - 1, 0, depth + 1), max_distance(x, y + 1, 2, depth + 1), max_distance(x + 1, y, 1, depth + 1)) + 1
        if dir == 2:
            value = max(max_distance(x, y + 1, 2, depth + 1), max_distance(x + 1, y, 1, depth + 1)) + 1
        output[y][x][dir] = value
        return value
    max_distance(0, 0, 2, 0)
    return max([x if x is not None else -1 for x in output[0][0]])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )

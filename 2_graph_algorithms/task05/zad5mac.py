# Paweł Piechnik
# Pracuje na reprezentacji macierzowej, puszczam algorytm dijkstry od końca, jeśli znajdę punkt osobliwości to przerywam algorytm i zapisuję go, jeśli dojdę do początku to zwracam drogę, a jeśli żadna z tych 2 rzeczy się nie wydarzy to zwracam None (nie ma takiej ścieżki). Potem puszczam ten algorytm od początku i jeśli znajdę punkt osobliwości to dodaje odległości między początkiem a nim i między końcem a zapisanym wcześniej. Złożoność to O(N^2)
from zad5testy import runtests


def dijkstraM(n, M, start, end, S):
    d_s = [float("inf") for _ in range(n)]  # distance from start
    visited_s = [False for _ in range(n)]

    d_e = [float("inf") for _ in range(n)]  # distance from end
    visited_e = [False for _ in range(n)]

    d_s[start] = 0
    d_e[end] = 0

    nspfe = float("inf")  # nearest singularity point from end
    # going from end
    for _ in range(n):  # this for is to process all existing touched vertices
        u = -1
        distance = float("inf")
        # searches for the unvisited vertex with the lowest actual distance (touched by the for below) to process
        for i in range(n):
            if not visited_e[i] and distance > d_e[i]:
                u = i
                distance = d_e[i]

        # processes that vertex
        visited_e[u] = True
        # for each of its neighbours if path from u to v is shorter than previous it change it
        for v in range(n):
            if M[u][v] >= 0 and d_e[v] > d_e[u] + M[u][v]:
                d_e[v] = d_e[u] + M[u][v]

        # if it reached start vertex return distance from end to start
        if u == start:
            return d_e[u]

        # if it reached any singularity (the nearest form end) save that point and break
        if u in S:
            nspfe = u
            break

    # if it doesn't return any value and nspe is inf there is no path from start to end
    if nspfe == float("inf"):
        return None

    # going from start
    for _ in range(n):  # this for is to process all existing touched vertices
        u = -1
        distance = float("inf")
        # searches for the unvisited vertex with the lowest actual distance (touched by the for below) to process
        for i in range(n):
            if not visited_s[i] and distance > d_s[i]:
                u = i
                distance = d_s[i]

        # processes that vertex
        visited_s[u] = True
        # for each of its neighbours if path from u to v is shorter than previous it change it
        for v in range(n):
            if M[u][v] >= 0 and d_s[v] > d_s[u] + M[u][v]:
                d_s[v] = d_s[u] + M[u][v]

        # if it reached nspfe there wasn't any singularity point on the way or if it reached any singularity point (the nearest from the start) it adds distance from start to that sp and form end to nspfe
        if u == nspfe or u in S:
            return d_s[u] + d_e[nspfe]


def spacetravel(n, E, S, a, b):
    M = [[-1 for _ in range(n)] for _ in range(n)]
    for edge in E:
        M[edge[0]][edge[1]] = edge[2]
        M[edge[1]][edge[0]] = edge[2]

    distance = dijkstraM(n, M, a, b, S)

    return distance


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(spacetravel, all_tests=True)

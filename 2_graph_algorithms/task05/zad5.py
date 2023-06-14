# Paweł Piechnik
# Pracuje na reprezentacji listowej, puszczam algorytm dijkstry od końca, jeśli znajdę punkt osobliwości to przerywam algorytm i zapisuję go, jeśli dojdę do początku to zwracam drogę, a jeśli żadna z tych 2 rzeczy się nie wydarzy to zwracam None (nie ma takiej ścieżki). Potem puszczam ten algorytm od początku i jeśli znajdę punkt osobliwości to dodaje odległości między początkiem a nim i między końcem a zapisanym wcześniej punktem osobliwości. Złożoność to O(ElogE)

from zad5testy import runtests
from queue import PriorityQueue


def dijkstra(n, G, start, end, S):
    d_s = [float("inf") for _ in range(n)]
    q_s = PriorityQueue()
    d_e = [float("inf") for _ in range(n)]
    q_e = PriorityQueue()

    q_s.put((0, start))
    q_e.put((0, end))

    nspfe = float("inf")  # nearest singularity point from end

    # going from end
    while not q_e.empty():
        distance, u = q_e.get()
        # if vertex from top of queue is unvisited processes it (save its distance)
        if d_e[u] == float("inf"):
            d_e[u] = distance
            # for each of its unvisited neighbours puts them to priority queue
            for v, w in G[u]:  # v - vertex, w - distance from u to v
                if d_e[v] == float("inf"):
                    q_e.put((d_e[u] + w, v))

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
    while not q_s.empty():
        distance, u = q_s.get()
        # if vertex from top of queue is unvisited processes it (save its distance)
        if d_s[u] == float("inf"):
            d_s[u] = distance
            # for each of its unvisited neighbours puts them to priority queue
            for v, w in G[u]:  # v - vertex, w - distance from u to v
                if d_s[v] == float("inf"):
                    q_s.put((d_s[u] + w, v))

        # if it reached nspfe there wasn't any singularity point on the way or if it reached any singularity point (the nearest from the start) it adds distance from start to that sp and form end to nspfe
        if u == nspfe or u in S:
            return d_s[u] + d_e[nspfe]


def spacetravel(n, E, S, a, b):
    G = [[] for _ in range(n)]
    for edge in E:
        G[edge[0]].append((edge[1], edge[2]))
        G[edge[1]].append((edge[0], edge[2]))

    distance = dijkstra(n, G, a, b, S)

    return distance


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(spacetravel, all_tests=True)

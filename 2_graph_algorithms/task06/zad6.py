# Paweł Piechnik
# Tworzę sobie graf dwudzielny, gdzie "lewa część" zawiera wierzchołki którymi są pracownicy a "prawa" to maszyny. Dodaję krawędzie jednokierunkowe od pracowników do maszyn, które umieją obsługiwać. Dodaje jeszcze "s" z którego wychodzą krawędzie do wszystkich pracowników oraz "t" do którego wchodzą krawędzie ze wszystkich maszyn. Wszystkie krawędzie mają wagę 1. Puszczam algorytm forda fulkersona z s do t. Maksymalny przepływ jest równy maksymalnej liczbie pracujących na raz pracowników. Złożoność to O(n^3)

from zad6testy import runtests


def bfs(M, s, t, parents):
    Q = []
    n = len(M)

    visited = [False for _ in range(n)]
    visited[s] = True
    Q.append(s)

    while len(Q) != 0:
        u = Q.pop()
        for v in M[u]:
            if not visited[v]:
                parents[v] = u
                visited[v] = True
                Q.append(v)
        if visited[t]:
            return True
    return False


def ford_fulkerson(M, s, t):
    n = len(M)
    parents = [None for _ in range(n)]
    max_flow = 0
    while bfs(M, s, t, parents):
        # updetes residual network
        current_vertex = t
        while current_vertex != s:
            M[parents[current_vertex]].remove(current_vertex)
            M[current_vertex].append(parents[current_vertex])
            current_vertex = parents[current_vertex]
        max_flow += 1
    return max_flow


def binworker(M):
    n = len(M)
    # machines -> [0,n]
    GRAPH = [[2 * n + 2] for _ in range(n + 1)]
    # workers -> [n+1,2n]
    for i in range(n):
        GRAPH.append(M[i])
    # s -> 2n+1
    GRAPH.append([i for i in range(n + 1, 2 * n + 1)])
    # t -> 2n+2
    GRAPH.append([])

    return ford_fulkerson(GRAPH, 2 * n + 1, 2 * n + 2)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(binworker, all_tests=False)

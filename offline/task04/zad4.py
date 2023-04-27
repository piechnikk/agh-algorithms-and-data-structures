# Paweł Piechnik
# Znajduję najkrótszą ścieżke z wykorzystaniem bfs i odcinam po kolei krawędzie od końca i znowu puszczam bfs. Jeśli najkrótsza ścieżka po kolejnym puszczeniu bfs-a jest dłuższa niż ta po 1. to zwracam krotkę z odciętą krawędzią.
# Złożoność O((V+E)*E) gdzie V to wierzchołki a E to krawędzie

from zad4testy import runtests
import queue

Graph = list[list[int]]


def bfs(G: Graph, i: int, t: int, banned: tuple = None) -> None:
    n = len(G)
    visited = [False for _ in range(n)]
    distance = [-1 for _ in range(n)]
    parents = [None for _ in range(n)]
    q = queue.Queue()

    visited[i] = True
    distance[i] = 0
    parents[i] = None
    q.put(i)
    while not q.qsize() == 0:
        v = q.get()
        for p in G[v]:
            if not visited[p] and (
                banned is None or p not in banned or v not in banned
            ):  # banned is a tuple with a cutted off edge
                q.put(p)
                visited[p] = True
                distance[p] = distance[v] + 1
                parents[p] = v
                if p == t:
                    return visited, distance, parents
    return visited, distance, parents


def longer(G: Graph, s: int, t: int) -> tuple:
    visited, distance, parents = bfs(G, s, t)
    # if there is no path between s and t return None
    if not visited[t]:
        return None

    original_distance = distance[t]

    # creating a path from t to s
    parent = parents[t]
    path = [t]
    while parent != None:
        path.append(parent)
        parent = parents[parent]

    # for each edge in shortest path it banned it for single pass and if there is longer path with banned edge or if it is no path it returns that banned path otherwise it returns None
    for i in range(len(path) - 1):
        visited, distance, parents = bfs(G, s, t, (path[i], path[i + 1]))
        if not visited[t] or original_distance < distance[t]:
            return (path[i], path[i + 1])

    return None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(longer, all_tests=True)

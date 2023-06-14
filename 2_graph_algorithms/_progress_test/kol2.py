# # Paweł Piechnik
# # Tworzę tablicę ze wszystkimi wagami, sortuję ją a potem mam pętle po wszystkich wierzchołkach w której mam kolejną pętle w której ograniczam wagi od góry i od dołu. Wywołuje za każdym razem bfsa z ograniczoną widocznością krawędzi w którym dodaje wagi przebytych krawędzi.
# from kol2testy import runtests


# def bfs(G, s, minW, maxW):
#     Q = []
#     n = len(G)

#     parent = [None for _ in range(n)]
#     visited = [False for _ in range(n)]
#     weight = 0

#     visited[s] = True
#     parent[s] = None
#     Q.append(s)

#     while len(Q) > 0:
#         u = Q.pop()
#         for i in range(len(G[u])):
#             v = G[u][i][0]
#             if not visited[v] and (G[u][i][1] >= minW and G[u][i][1] <= maxW):
#                 weight += G[u][i][1]
#                 parent[v] = u
#                 visited[v] = True
#                 Q.append(v)

#     return False in visited, weight, parent


# def beautree(G):
#     n = len(G)
#     Graph = []
#     for i in range(n):
#         for j in range(len(G[i])):
#             if (G[i][j][0], i, G[i][j][1]) not in Graph:
#                 Graph.append((i, G[i][j][0], G[i][j][1]))
#     Graph.sort(key=lambda i: i[2])

#     weights = []
#     for i in range(n):
#         for j in range(len(G[i])):
#             if G[i][j][1] not in weights:
#                 weights.append(G[i][j][1])
#     weights.sort()

#     min_weight = float("inf")
#     for v in range(n):
#         minW = 0
#         maxW = len(weights) - 1
#         for w in range(len(weights) - 1):
#             not_ok, weight, parent = bfs(G, v, weights[minW], weights[maxW])
#             if not_ok:
#                 break
#             if weight < min_weight:
#                 min_weight = weight
#             minW += 1
#         for w in range(len(weights) - 1):
#             not_ok, weight, parent = bfs(G, v, weights[minW], weights[maxW])
#             if not_ok:
#                 break
#             if weight < min_weight:
#                 min_weight = weight
#             maxW -= 1
#         minW = 0
#         maxW = len(weights) - 1
#         for w in range(len(weights) - 1):
#             not_ok, weight, parent = bfs(G, v, weights[minW], weights[maxW])
#             if not_ok:
#                 break
#             if weight < min_weight:
#                 min_weight = weight
#             maxW -= 1
#         for w in range(len(weights) - 1):
#             not_ok, weight, parent = bfs(G, v, weights[minW], weights[maxW])
#             if not_ok:
#                 break
#             if weight < min_weight:
#                 min_weight = weight
#             minW += 1
#     if min_weight < float("inf"):
#         return min_weight
#     else:
#         return None


# # zmien all_tests na True zeby uruchomic wszystkie testy
# runtests(beautree, all_tests=True)

from kol2testy import runtests


def dfs(G):
    n = len(G)
    weight = 0
    vis = [False] * n

    def visit(u):
        nonlocal weight
        vis[u] = True
        for v, w in G[u]:
            if not vis[v]:
                weight += w
                visit(v)

    visit(0)
    for visited in vis:
        if not visited:
            return False

    return weight


def beautree(G):
    n = len(G)

    edges = []
    for u in range(n):
        for v, w in G[u]:
            edges.append((u, v, w))
            edges.sort(key=lambda it: it[2])

    min_weight = float("inf")

    graph = [[] for _ in range(n)]

    for u, v, w in edges[0 : 2 * (n - 1)]:
        graph[u].append((v, w))

    for i in range(0, len(edges) - 2 * n, 2):
        weight = dfs(graph)
        if weight and weight < min_weight:
            min_weight = weight
            break

        min_e = edges[i]
        max_e = edges[i + 2 * (n - 1)]

        graph[min_e[0]].remove((min_e[1], min_e[2]))
        graph[min_e[1]].remove((min_e[0], min_e[2]))
        graph[max_e[0]].append((max_e[1], max_e[2]))
        graph[max_e[1]].append((max_e[0], max_e[2]))

    return min_weight if min_weight < float("inf") else None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(beautree, all_tests=True)

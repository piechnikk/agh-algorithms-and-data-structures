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

    min_weight = float('inf')

    graph = [[] for _ in range(n)]

    for u, v, w in edges[0:2*(n-1)]:
      graph[u].append((v, w))

    for i in range(0, len(edges) - 2*n, 2):
        weight = dfs(graph)
        if weight and weight < min_weight:
            min_weight = weight
            break

        min_e = edges[i]
        max_e = edges[i+2*(n-1)]

        graph[min_e[0]].remove((min_e[1], min_e[2]))
        graph[min_e[1]].remove((min_e[0], min_e[2]))
        graph[max_e[0]].append((max_e[1], max_e[2]))
        graph[max_e[1]].append((max_e[0], max_e[2]))

    return min_weight if min_weight < float('inf') else None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( beautree, all_tests = True )

from dijkstra import dijkstra


def path(M, s, t):
    _, parent = dijkstra(M, s)
    path = []
    u = t
    while u != s:
        path.append(u)
        u = parent[u]
    path.append(s)
    path = path[::-1]
    return path

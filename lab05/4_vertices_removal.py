# remove all vertices one by one to keep the graph connected


def dfs_visit(G, s, visited, w):
    visited[s] = True
    n = len(G)
    for v in range(n):
        if not visited[v]:
            dfs_visit(G, v, visited, w)
        w.append(s)


def unzip(G):
    n = len(G)
    w = []
    visited = [False for _ in range(n)]
    dfs_visit(G, 0, visited, w)
    return w

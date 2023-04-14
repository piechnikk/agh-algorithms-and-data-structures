# checks if graph is bipartite


def dfs_visit(M, s, c, colors):
    colors[s] = c
    c = 2 if c == 1 else 1
    n = len(M)
    for i in range(n):
        if M[s][i]:
            if colors[i] == 0:
                r = dfs_visit(M, i, c, colors)
                if r is False:
                    return False
            elif colors[i] != c:
                return False
    return True


def is_bipartite(M):
    n = len(M)
    colors = [0 for _ in range(n)]
    for v in range(n):
        if colors[v] == 0:
            if dfs_visit(M, v, 1, colors):
                return False
    return True

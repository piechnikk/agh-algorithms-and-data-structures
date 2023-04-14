# coherent components

import queue


def bfs_visit(G, i, visited):
    q = queue.Queue()
    visited[i] = True
    q.put(i)
    while not q.empty():
        v = q.get()
        for p in range(G[v]):
            if not visited[p]:
                q.put(p)
                visited[p] = True


def c_components(G):
    n = len(G)
    visited = [False for _ in range(n)]
    c = 0
    for i in range(n):
        if not visited[i]:
            c += 1
            bfs_visit(G, i, visited)
    return c

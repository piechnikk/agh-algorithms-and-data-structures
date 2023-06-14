from queue import PriorityQueue


# https://replit.com/@kzzzf/ASD23r2
# https://replit.com/join/xbzjhivfzh-kzzzf
inf = float("inf")


def dijkstra(M, s):
    n = len(M)
    d = [inf for _ in range(n)]
    parent = [None for _ in range(n)]
    q = PriorityQueue()

    q.put((0, s, -1))

    while not q.empty():
        distance, u, p = q.get()
        if d[u] == inf:
            d[u] = distance
            parent[u] = p
            for v, w in M[u]:
                if d[v] == inf:
                    q.put((d[u] + w, v, u))
    return d, parent


def dijkstraM(M, s):
    n = len(M)
    d = [inf for _ in range(n)]
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]

    d[s] = 0

    for _ in range(n):
        u = -1
        distance = inf
        for i in range(n):
            if not visited[i] and distance > d[i]:
                u = i
                distance = d[i]

        visited[u] = True
        for v in range(n):
            if M[u][v] >= 0 and d[v] > d[u] + M[u][v]:
                parent[v] = u
                d[v] = d[u] + M[u][v]
    return d, parent


def path(M, s, t):
    parent = dijkstra(M, s)
    path = []
    u = t
    while u != s:
        path.append(u)
        u = parent[u]
    path = path[::-1]
    return path

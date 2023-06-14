# ford fulkerson algorithm

from queue import Queue


def bfs(M, s, t, parents):
    Q = Queue()
    n = len(M)

    visited = [False for _ in range(n)]
    visited[s] = True
    Q.put(s)

    while not Q.qsize() == 0:
        u = Q.get()
        for v in range(n):
            if not visited[v] and M[u][v] > 0:
                parents[v] = u
                visited[v] = True
                Q.put(v)
        if visited[t]:
            return True
    return False


def ford_fulkerson(M, s, t):
    n = len(M)
    parents = [None for _ in range(n)]
    max_flow = 0
    while bfs(M, s, t, parents):
        current_flow = float("inf")

        # finds maximum flow in the found path between s and t
        current_vertex = t
        while current_vertex != s:
            current_flow = min(current_flow, M[parents[current_vertex]][current_vertex])
            current_vertex = parents[current_vertex]
        max_flow += current_flow

        # updetes residual network
        current_vertex = t
        while current_vertex != s:
            M[parents[current_vertex]][current_vertex] -= current_flow
            M[current_vertex][parents[current_vertex]] += current_flow
            current_vertex = parents[current_vertex]

    return max_flow


M = [
    [0, 11, 12, 17, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 14, 0, 0, 0, 0],
    [0, 0, 0, 0, 8, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 9, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 10, 0],
    [0, 0, 0, 0, 0, 0, 6, 9, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]
print(ford_fulkerson(M, 0, 9))

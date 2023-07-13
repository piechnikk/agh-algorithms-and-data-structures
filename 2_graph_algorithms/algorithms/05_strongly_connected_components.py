# runs dfs saving processing times, reverses direction of all edges, runs dfs selecting starting vertices in descending order of processing times (which it has not yet processed) from the previous execution, in a given dfs_visit form a strongly connected component
# complexity like dfs: O(V+E) - list representation, O(V^2) - matrix representation

Graph = list[list[bool]]

def get_neighbours(G: Graph, v: int) -> list[int]:
    n = len(G)
    neighbours: list[int] = []
    for i in range(n):
        if G[v][i]:
            neighbours.append(i)
    return neighbours


def dfs(G: Graph, times: list):
    def dfs_visit(G: Graph, u: int) -> None:
        nonlocal time
        time += 1
        visited[u] = True
        neighbours = get_neighbours(G, u)
        for v in neighbours:
            if not visited[v]:
                dfs_visit(G, v)
        times[u] = (time, u)

    n = len(G)
    visited = [False for _ in range(n)]

    time = 0
    for u in range(n):
        if not visited[u]:
            dfs_visit(G, u)

    return times


def dfs2(G: Graph):
    def dfs_visit(G: Graph, u: int) -> None:
        str_conn_cmp = []
        visited[u] = True
        neighbours = G[u]
        str_conn_cmp.append(u)
        for v in neighbours:
            if not visited[v]:
                dfs_visit(G, v)
        return str_conn_cmp

    n = len(G)
    visited = [False for _ in range(n)]
    components = []

    for u in range(n):
        if not visited[u]:
            components.append(dfs_visit(G, u))

    return components


def str_cmp(G):
    n = len(G)
    reversed_G = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            reversed_G[i].append(G[j][i])

    times = [(-1, None) for _ in range(n)]
    dfs(G, times)
    times.sort(key=lambda item: item[0], reverse=True)

    return dfs2(G)


G = [[2], [0], [1], [2, 5, 8], [3], [4, 6, 7], [3], [10], [7], [8], [2, 9]]

print(str_cmp(G))

# depth-first search, goes from vertex s and processes each neighbor, goes recursively
# complexity: O(V+E) - list representation, O(V^2) - matrix representation
Graph = list[list[bool]]

def get_neighbours(G: Graph, v: int) -> list[int]:
    """Returns list of vertices connected to v."""
    n = len(G)
    neighbours: list[int] = []
    for i in range(n):
        if G[v][i]:
            neighbours.append(i)
    return neighbours


def dfs(G: Graph):
    """DFS

    Searches a tree structure in a graph and returns time from s to each vertex and parent of each vertex.
    """

    def dfs_visit(G: Graph, u: int) -> None:
        """Handling subsequent vertices for the dfs algorithm"""
        nonlocal time
        time += 1
        visited[u] = True
        times[u] = time
        neighbours = get_neighbours(G, u)
        for v in neighbours:
            if not visited[v]:
                parent[v] = u
                dfs_visit(G, v)

    n = len(G)
    parent = [None for _ in range(n)]
    visited = [False for _ in range(n)]
    times = [-1 for _ in range(n)]

    time = 0
    # dfs_visit(G, s) # s - startowy wierzchołek
    for u in range(n):
        if not visited[u]:
            dfs_visit(G, u)

    return times, parent


G: Graph = [
    [None, True, True, False, False, False, False, False],
    [True, None, False, False, True, False, False, False],
    [True, False, None, True, False, True, False, False],
    [False, False, True, None, True, False, False, False],
    [False, True, False, False, None, True, False, False],
    [False, False, True, False, True, None, True, False],
    [False, False, False, False, False, True, None, True],
    [False, False, False, False, False, False, True, None],
]
print(dfs(G))

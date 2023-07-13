# runs dfs and after processing each vertex appends it to the beginning of the created list
# complexity like dfs: O(V+E) - list representation, O(V^2) - matrix representation
Graph = list[list[bool]]

def get_neighbours(G: Graph, v: int) -> list[int]:
    """Returns list of vertices connected to v."""
    n = len(G)
    neighbours: list[int] = []
    for i in range(n):
        if G[v][i]:
            neighbours.append(i)
    return neighbours


def topologic_sort(G: Graph) -> list:
    def dfs_visit(G: Graph, u: int) -> None:
        neighbours = get_neighbours(G, u)
        for v in neighbours:
            if not visited[v]:
                dfs_visit(G, v)
        sorted.append(u)
        visited[u] = True

    n = len(G)
    visited = [False for _ in range(n)]
    sorted = []

    for u in range(n):
        if not visited[u]:
            dfs_visit(G, u)

    return sorted[::-1]


G: Graph = [
    [False, True, True, False, False, False, False, False],
    [False, False, True, True, False, False, False, False],
    [False, False, False, False, True, False, False, False],
    [False, False, False, False, False, True, False, False],
    [False, False, False, False, False, True, False, False],
    [False, False, False, False, False, False, True, True],
    [False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False],
]
print(topologic_sort(G))

# finds bridge in graph
# runs dfs, for each v saves his meeting time d(v)
# for each vertex v calculate low(v) = min(d(v),min(d(u)), min(low(w))) [v is reverse edge for u, w is v's child in dfs tree]
# bridges are edges {v,p(v)} [p(v) is parent in dfs tree] such that d(v) = low(v).
# complexity like bfs: O(V+E) - list representation, O(V^2) - matrix representation

Graph = list[list[bool]]

def get_neighbours(G: Graph, v: int) -> list[int]:
    """Returns list of vertices connected to v."""
    n = len(G)
    neighbours: list[int] = []
    for i in range(n):
        if G[v][i]:
            neighbours.append(i)
    return neighbours


def find_bridges(G: Graph):
    """Returns bridges in graph"""

    def dfs_visit(G: Graph, s: int, p: int) -> int:
        nonlocal time
        time += 1
        times[s] = time
        visited[s] = True
        lows[s] = time

        neighbours = get_neighbours(G, s)
        # for each vertex that if is not visited runs dfs_visit that goes through each neighbour of this vertex, saves his meeting time and calculate low
        for v in neighbours: 
            if not visited[v]:
                low_child = dfs_visit(G, v, s)
                if low_child < lows[s]:
                    lows[s] = low_child
            elif v != p and lows[v] < lows[s]:
                lows[s] = lows[v]
        if s > 0 and times[s] == lows[s]:
            bridges.append(s)
        return lows[s]

    n = len(G)
    time = 0
    visited = [False for _ in range(n)]
    times = [0 for _ in range(n)]
    lows = [0 for _ in range(n)]
    bridges: list[int] = []

    for v in range(n):
        if not visited[v]:
            dfs_visit(G, v, None)

    return bridges


G: Graph = [
    [None, True, False, False, False, False, True, False],
    [True, None, True, False, False, False, False, False],
    [False, True, None, True, False, False, True, False],
    [False, False, True, None, True, True, False, False],
    [False, False, False, True, None, True, False, False],
    [False, False, False, True, True, None, False, False],
    [True, False, True, False, False, False, None, True],
    [False, False, False, False, False, False, True, None],
]
print(find_bridges(G))

# checks if graph is bipartite
Graph = list[list[bool]]


def dfs_visit(M: Graph, s: int, c: int, colors: list[int]) -> bool:
    """It paints vertex s on color c and its adjacent vertices on opposite color than c.
    If any neighbour is colored on the same color as s it returns False otherwise True.

    s: index of the handled vertex
    c: the color it paints vertex s (1 or 2)
    colors: list with the color of each vertex
    """
    colors[s] = c
    c = 2 if c == 1 else 1
    n = len(M)

    # for each neighbour of vertex s if it is uncolored it runs dfs_visit
    for i in range(n):
        if M[s][i]:
            if colors[i] == 0:
                r = dfs_visit(M, i, c, colors)
                if r is False:
                    return False

            # if neighbour is colored on the same color as s it returns False
            elif colors[i] != c:
                return False
    return True


def is_bipartite(M: Graph) -> bool:
    """Checks if graf is bipartite"""
    n = len(M)
    colors = [0 for _ in range(n)]

    # for each uncolored vertex it runs dfs_visit
    for v in range(n):
        if colors[v] == 0:
            if dfs_visit(M, v, 1, colors):
                return False
    return True

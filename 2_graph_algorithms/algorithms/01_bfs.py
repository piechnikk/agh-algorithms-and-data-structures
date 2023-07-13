# releases a "shockwave from s" visiting successive neighbors. put s on the queue and while the queue is not empty I pull the vertex from the queue, process it and add to the queue all its unvisited neighbors
# complexity: O(V+E) - list representation, O(V^2) - matrix representation
import queue

Graph = list[list[bool]]

def get_neighbours(G: Graph, v: int) -> list[int]:
    """Returns list of vertices connected to v."""
    n = len(G)
    neighbours: list[int] = []
    for i in range(n):
        if G[v][i]:
            neighbours.append(i)
    return neighbours


def bfs(G: Graph, s: int):  # s - index of starting vertex
    """BFS

    Searches a tree structure in a graph and returns distance from s to each vertex and parent of each vertex.
    """
    Q = queue.Queue()
    n = len(G)

    distance = [-1 for _ in range(n)]
    parent = [None for _ in range(n)]
    visited = [False for _ in range(n)]

    distance[s] = 0
    visited[s] = True
    parent[s] = None
    Q.put(s)

    while not Q.qsize() == 0:
        u = Q.get()
        neighbours = get_neighbours(G, u)
        for v in neighbours:
            if not visited[v]:
                distance[v] = distance[u] + 1
                parent[v] = u
                visited[v] = True
                Q.put(v)

    return distance, parent


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
print(bfs(G, 0))

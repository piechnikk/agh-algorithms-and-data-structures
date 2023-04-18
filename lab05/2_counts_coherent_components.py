# counts coherent components of an incoherent graph
import queue

Graph = list[list[int]]  # for each vertex contains list of connected vertices


def bfs(G: Graph, i: int, visited: list[int]) -> None:
    """Breadth-first search."""
    q = queue.Queue()
    visited[i] = True
    q.put(i)
    while not q.qsize() == 0:
        v = q.get()
        for p in range(G[v]):
            if not visited[p]:
                q.put(p)
                visited[p] = True


def c_components(G: Graph) -> int:
    """Returns number of coherent components in an incoherent graph."""
    n = len(G)
    visited = [False for _ in range(n)]
    c = 0
    # for each vertex if it's not visited, runs bfs, which finds a coherent component that contains that vertex
    for i in range(n):
        if not visited[i]:
            c += 1
            bfs(G, i, visited)
    return c

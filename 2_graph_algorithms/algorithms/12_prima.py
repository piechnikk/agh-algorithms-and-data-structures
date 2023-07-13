# v - starting vertex, very similar to dijkstra
# put all vertices in priority queue with weight inf
# change the weight of v to 0
# while the vertices are in the queue: remove vertex u with minimal weight from the queue, for each edge {u, x} if weight w(u, x) < weight x in the queue then change weight x to w(u, x) (update parent) (put another tuple in the priority queue)

from queue import PriorityQueue
inf = float("inf")
def prima(M, s):
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
                    q.put((w, v, u))
    return d, parent
G = [
    [(1,1),(4,5),(5,8)],
    [(0,1),(2,3)],
    [(1,3),(3,6),(4,4)],
    [(2,6),(4,2)],
    [(0,5),(2,4),(3,2),(5,7)],
    [(0,8),(4,7)]
]
print(prima(G,0))
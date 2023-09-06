from egz1Atesty import runtests
from queue import PriorityQueue
inf = float("inf")

def gold(G, V, s, t, r):
    def dijkstra(G, s, r=0):
        n = len(G)
        d = [inf for _ in range(n)]
        q = PriorityQueue()

        q.put((0, s))

        while not q.empty():
            distance, u = q.get()
            if d[u] == inf:
                d[u] = distance
                for v, w in G[u]:
                    if d[v] == inf:
                        q.put((d[u] + w if r == 0 else d[u] + (2 * w) + r, v))
        return d

    n = len(G)
    d = dijkstra(G, s)
    d2 = dijkstra(G, t, r)
    
    return min(d[i] + d2[i] - V[i] for i in range(n))


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = True )
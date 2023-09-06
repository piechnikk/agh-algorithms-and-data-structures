# Paweł Piechnik
# Wykonuje najpierw algorytm dijksty, który mi zwraca najmniejszy koszt bez rabowania, a później wykonuje len(V) razy algorytm dijksty rozważając każdy rabunek (w każdym takim przejściu ustawiam wartość początkową na odległość z s do rabowanego zamku (mam ją po pierwszym przejściu dijkstry) - ilość złota w rabowanym zamku a później znowu robie dijkstre ale uwzględniając podwójny koszt i łapówki) złożoność to O(VElogV)
from egz1Atesty import runtests

from queue import PriorityQueue

inf = float("inf")


def dijkstra(G, s):
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
                    q.put((d[u] + w, v))
    return d

def dijkstra2(G, s, t, startcost, r): # (graf, start, koniec, wartość w starcie, łapówka)
    n = len(G)
    d = [inf for _ in range(n)]
    q = PriorityQueue()

    q.put((startcost, s))

    while not q.empty():
        distance, u = q.get()
        if d[u] == inf:
            d[u] = distance
            if u == t:
                return d[u]
            for v, w in G[u]:
                if d[v] == inf:
                    q.put((d[u] + (2*w)+r, v))
    
    return d[u]

def gold(G, V, s, t, r):
    n = len(G)
    d = dijkstra(G, s)

    return min([d[t]]+[dijkstra2(G, i, t, d[i] - V[i], r) if V[i]>0 else inf for i in range(n)])


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = True )
# returns the set of edges that make up the MST without creating a tree structure
# sort edges by weights, A = [], browse edges in order of non-increasing weights, if A u {e} does not contain a cycle then A.append(e), return A
# complexity O(ElogV)

def kruskal(G):
    # finds the number of vertices in graph  
    maxedge = max(G, key=lambda x: max(x[0], x[1]))
    n = max(maxedge[0], maxedge[1]) + 1

    s = list(range(n))
    r = [0] * n

    def find(u):
        if s[u] == u:
            return u
        s[u] = find(s[u])
        return s[u]

    def union(u, v):
        ur, vr = find(u), find(v)
        if ur != vr:
            if r[ur] > r[vr]:
                s[vr] = ur
            elif r[vr] > r[ur]:
                s[ur] = vr
            else:
                s[vr] = ur
                r[ur] += 1

    G.sort(key=lambda a: a[2])

    MST = []
    for u, v, t in G:
        if find(u) != find(v):
            union(u, v)
            MST.append((u, v, t))
    return MST


# G = [(1, 2, 3), (2, 3, 2), (2, 4, 7), (1, 3, 5), (1, 5, 9), (5, 4, 6)]

# print(kruskal(G))

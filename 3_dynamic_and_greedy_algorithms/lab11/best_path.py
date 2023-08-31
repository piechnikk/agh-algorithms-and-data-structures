# the best path in the tree
# we have an undirected graph G which is a tree 
# each edge has some weight (can be negative)
# we are looking for a path whose sum of weights is maximum

# I go through the layers of the tree one by one and calculate the 2 most expensive paths with a starting point in i (i is the currently calculated vertex) that go down the tree
# then I take the largest sum of these 2 paths

def best_path(G):
    v = len(G)
    maxims = [[None, None] for _ in range(v)]

    def twomax(A):
        A = list(A)
        if len(A) == 1:
            return [A[0], 0]
        maximum = [A[0], A[1]] if A[0]>A[1] else [A[1], A[0]]
        for i in range(2,len(A)):
            if A[i] > maximum[1]:
                maximum[1] = A[i]
                if maximum[1]>maximum[0]:
                    maximum[0], maximum[1] = maximum[1], maximum[0]
        return maximum

    def f(i, parent = None):
        maxims[i] = twomax(f(neighbour[0], i)+neighbour[1] if neighbour[0] != parent else 0 for neighbour in G[i])
        return maxims[i][0]
    
    f(0)
    return sum(max(maxims, key=lambda x: x[0]+x[1]))

G = [
    [(1,10),(2,15)],
    [(0,10)],
    [(3,-5),(4,5),(0,15)],
    [(5,20),(2,-5)],
    [(2,5)],
    [(3,20)],
]
G1 = [
    [(1,10),(2,-30)],
    [(0,10)],
    [(3,-5),(4,5),(0,-30)],
    [(5,15),(2,-5)],
    [(2,5)],
    [(3,15)],
]
print(best_path(G))
print(best_path(G1))





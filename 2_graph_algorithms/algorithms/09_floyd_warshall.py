# finds the shortest distance from each to each vertex 
# complexity O(V^3)

def floyd_warshall(G):
    n = len(G)
    dis = [[float("inf") for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                dis[j][k] = min(dis[j][k], G[j][i] + G[i][k])
    return dis

# there is a directed graph G, find cycle with the smallest sum of weight.
def solve(G):
    n = len(G)
    dis = floyd_warshall(G)
    ans = -float("inf")
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            ans = min(ans, dis[i][j] + dis[j][i])
    return ans

G = [
    [0, 1, 2],
    [2, 0, 2],
    [1, 1, 0],
]
print(floyd_warshall(G))
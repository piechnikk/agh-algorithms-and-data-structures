# there is a directed graph G, find cycle with the smallest sum of weight.


def floyd_warshall(G):
    n = len(G)
    dis = [[float("inf") for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                dis[j][k] = min(dis[j][k], dis[j][i] + dis[i][k])
    return dis


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

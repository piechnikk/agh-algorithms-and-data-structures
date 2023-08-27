# we have a chessboard of size n x n
# a figure stands in the top left corner
# it can move only one field down or one field to the right
# it wants to get to the bottom roght corner
# each field has a cost of standing on it
# find the cost of the cheapest path to bottom right corner

# solution-defining function:
# function f(x, y) -> |N, x and y are the current figurt coordinates, returns the minimum cost of getting from point (x, y) to (n, n)
# f(n, n) = 0
# f(x, y) = min(
#               C[x + 1][y] + f(x + 1, y),
#               C[x][y + 1] + f(x, y + 1)
#           )
# f(x, y) = inf when x > n or y > n


def path(C):
    n = len(C)
    costs = [[float("inf")] * n for _ in range(n)]
    costs[n - 1][n - 1] = 0
    for x in range(n - 1, -1, -1):
        for y in range(n - 1, -1, -1):
            if x == n-1 and y == n-1:
                continue
            down = right = float("inf")
            if x < n-1:
                right = costs[x + 1][y] + C[x + 1][y]
            if y < n-1:
                down = costs[x][y + 1] + C[x][y + 1]
            costs[x][y] = min(right, down)
    return costs[0][0]

# C - array with costs
def pathReq(C):
    n = len(C)
    costs = [[float("inf")] * n for _ in range(n)]
    costs[n-1][n-1] = 0
    def f(x,y):
        if(costs[x][y]!=float("inf")):
            return costs[x][y]
        if x<n-1 and y<n-1:
            return min(C[x+1][y]+f(x+1,y), C[x][y+1]+f(x,y+1))
        if x==n-1:
            return C[x][y+1]+f(x,y+1)
        if y==n-1:
            return C[x+1][y]+f(x+1,y)
    return f(0,0)

C = [
    [1,1,1,1],
    [2,1,1,3],
    [1,2,3,5],
    [1,3,1,1],
]
print(path(C))

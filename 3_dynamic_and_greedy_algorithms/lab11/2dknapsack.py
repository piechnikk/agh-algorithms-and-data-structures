def knapsack(T, w, h):
    n = len(T)
    dp = [[-float('inf')] * (w + 1) for _ in range(h + 1)]
    dp[0][0] = 0

    # T[w][h][c]
    for k in range(n):
        for i in range(h, -1, -1):
            for j in range(w, -1, -1):
                if dp[i][j] > -float(
                        'inf') and i + T[k][1] < h + 1 and j + T[k][0] < w + 1:
                    dp[i + T[k][1]][j + T[k][0]] = max(
                        dp[i + T[k][1]][j + T[k][0]], dp[i][j] + T[k][2])

    cost = -float('inf')
    for i in range(h + 1):
        for j in range(w + 1):
            if dp[i][j] > cost:
                cost = dp[i][j]

    return cost

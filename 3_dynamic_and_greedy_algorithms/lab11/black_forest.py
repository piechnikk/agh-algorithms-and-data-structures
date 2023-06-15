# we have table with trees wich each has its ow value, we cant cut two neighbouring trees. We fing max value of cutted trees

def czarny_las(C):
    n = len(C)
    dp = [[0, 0] for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][1] = dp[i - 1][0] + C[i - 1]
        dp[i][0] = max(dp[i - 1][1], dp[i - 1][0])
    return max(dp[n][0], dp[n][1])


print(czarny_las([1, 3, 7, 5, 6, 6, 2]))
print(czarny_las([10, 1, 1, 10]))

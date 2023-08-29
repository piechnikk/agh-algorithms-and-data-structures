# we have table with trees wich each has its ow value, we cant cut two neighbouring trees. We fing max value of cutted trees

def black_forest(C):
    n = len(C)
    dp = [[0, 0] for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][1] = dp[i - 1][0] + C[i - 1]
        dp[i][0] = max(dp[i - 1][1], dp[i - 1][0])
    return max(dp[n][0], dp[n][1])


print(black_forest([1, 3, 7, 5, 6, 6, 2]))
print(black_forest([10, 1, 1, 10]))

def black_forest_recursive(TREES):
    n = len(TREES)
    answers = [[None, None] for _ in range(n)]
    answers[0] = [TREES[0], 0]
    def f(i,lastCutted): # lastCutted: 1->True, 0->False
        if answers[i][lastCutted] != None:
            return answers[i][lastCutted]
        
        if lastCutted == 1:
            answers[i][lastCutted] = f(i-1, 0)
        else:
            answers[i][lastCutted] = max(f(i-1, 1) + TREES[i], f(i-1, 0))

        return answers[i][lastCutted]
    
    return f(n-1, 0)


print(black_forest_recursive([1, 3, 7, 5, 6, 6, 2]))
print(black_forest_recursive([10, 1, 1, 10]))
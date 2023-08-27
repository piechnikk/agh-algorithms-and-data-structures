# we have an amount and a set of face value coins C
# spend an amount T minimum number of coins

# e.g. T = 15
# C = {1, 5, 8}
# greedy  approach: coins: 8 -> 5 -> 1 -> 1 (4 coins, take the largest face value if possible)
# optimal approach: coins: 5 -> 5 -> 5 (3 coins, proof that the greedy model does not work)

# function f(T) = min([f(T - face value) + 1 for face value in C]) - for each face value we run f(T - face value) and choose the smallest one
# f(T) - returns the minimum number of coins needed to spend T
# f(0) = 0
# f(T) = inf, for T < 0

def change(T, C):
    n = len(C)
    coins = [float("inf")] * (T + 1)
    coins[0] = 0
    def f(T):
        if T<0:
            return float("inf")
        if coins[T]!=float("inf"):
            return coins[T]
        return min(f(T-C[i])+1 for i in range(n))
    return f(T)

C = [1,5,8]
print(change(15,C))
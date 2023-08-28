# we have a sample sequence, e.g.
# A = 0, 7, 3, 0, 2, 9
# and another, e.g.
# B = 3, 5, 1, 0, 7, 9, 11

# we are looking for the longest common subsequence:
# the solution is: 3, 0, 9 (from A it "removes" 0, 7, 2, and from B it "removes" 5, 1, 7, 11)

# A - sequence size n
# B - sequence size m

# f(i, j) - the longest common subsequence of the sequences A[1..i] and B[1..j]
# f(0, j) = 0
# f(i, 0) = 0
# f(i, j) = {
#               f(i - 1, j - 1) + 1, when A[i] == B[j],
#               max(f(i - 1, j), f(i, j - 1)), when A[i] != B[j],
#               0, when i == 0 or j == 0
# }

def lcs(A, B):
    n = len(A)
    m = len(B)
    answers = [[-float("inf")] * m for _ in range(n)]
        
    def f(i, j):
        if i < 0 or j < 0:
            return 0
        if answers[i][j] != -float("inf"):
            return answers[i][j]
        if A[i]==B[j]:
            answers[i][j] = f(i-1, j-1) + 1
        else:
            answers[i][j] = max(f(i-1, j), f(i, j-1))
        return answers[i][j]
    return f(n-1,m-1)


A = [0, 7, 3, 0, 2, 9]
B = [3, 5, 1, 0, 7, 9, 11]
print(lcs(A,B))
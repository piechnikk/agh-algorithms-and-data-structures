# we have arrays of start coordinates and end coordinates of blocks
# the blocks fall in the order as in the array
# how many blocks at least you have to remove to make each block fit into the previous one
# f(i) = the length of the longest subsequence of blocks ending in the i-th so that they form a sequence of contained blocks
# f(i) = max(f(j)+1 if B[i][0]>B[j][0] and B[i][1]<B[j][1] else 1 for j in range(i))
def falling_blocks(B):
    n = len(B)
    answers = [1] * n
    for i in range(1, n):
        answers[i] = max(answers[j]+1 if B[i][0]>B[j][0] and B[i][1]<B[j][1] else 1 for j in range(i))
    return n - max(answers)

print(falling_blocks([(1,2), (0,8), (1,7), (2,7), (3,4)]))
# runs dfs but on the way it removes the edges it walked over, after processing a given vertex it adds it to the beginning of the cycle (in an undirected and connected graph there is an euler cycle <=> each vertex has an even degree)
# complexity like dfs: O(V+E) - list representation, O(V^2) - matrix representation

Graph = list[list[bool]]

def euler_cycle(M: Graph) -> list[int]:
    n = len(M)
    M = [M[i][:] for i in range(n)]  # copies list
    # print(M)
    result = []
    dfs_visit(0, M, result)
    return result


def dfs_visit(v: int, M: Graph, result: list[int]) -> None:
    n = len(M)
    for i in range(n):
        if M[v][i] == True:
            M[v][i] = False
            M[i][v] = False
            dfs_visit(i, M, result)
    result.append(v)


G: Graph = [
    [False, True, True, False, False, False, False, False],
    [True, False, False, False, True, False, False, False],
    [True, False, False, True, False, True, False, False],
    [False, False, True, False, True, False, False, False],
    [False, True, False, False, False, False, False, False],
    [False, False, True, False, False, False, True, False],
    [False, False, False, False, False, True, False, True],
    [False, False, False, False, False, False, True, False],
]
print(euler_cycle(G))
G: Graph = [
    [False, True, True, False, False, False, False],
    [True, False, True, True, True, True, True],
    [True, True, False, True, True, True, True],
    [False, True, True, False, True, True, False],
    [False, True, True, True, False, True, False],
    [False, True, True, True, True, False, False],
    [False, True, True, False, False, False, False],
]
print(euler_cycle(G))

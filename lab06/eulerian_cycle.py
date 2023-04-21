# finds Eulerian cycle in graph given in matrix representation

Graph = list[list[bool]]


def euler_cycle(M: Graph) -> list[int]:
    n = len(M)
    M = [M[i][:] for i in range(n)]
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

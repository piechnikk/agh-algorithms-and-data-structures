# Paweł Piechnik
# Tworzę 2 tablice w jednej przechowuje jaka jest najdłuższa droga z danej komnaty do (n-1, n-1) kiedy weszło się z góry a w drugiej kiedy weszło się z dołu. Uruchamiam funkcje z punktu (0, 0), która idzie w każdym możliwym kierunku (zależnie czy przyszło się z góry czy z dołu i czy można wejść do danej komnaty). Złożoność to O(n^2)
from zad7testy import runtests

inf = float("inf")


def maze(L):
    n = len(L)

    # F1 - the longest route when we entered from top
    F1 = [[None for i in range(n)] for _ in range(n)]
    F1[n - 1][n - 1] = 0

    # F2 - the longest route when we entered from bottom
    F2 = [[None for i in range(n)] for _ in range(n)]
    F2[n - 1][n - 1] = 0

    answer = longest(L, F1, F2, (0,0))
    return answer if answer != -inf else -1

def longest(L, F1, F2, s, direction=1):
    n = len(L)
    r = s[0]    # actual row
    c = s[1]    # actual col
    
    # when it has calculated answer it returns it 
    if direction == 1:
        if F1[r][c] != None:
            return F1[r][c]
    if direction == 2:
        if F2[r][c] != None:
            return F2[r][c]
    if direction == 3:
        if F1[r][c] != None and F2[r][c] != None:
            return max(F1[r][c], F2[r][c])
    
    # if the chamber cannot be entered
    if L[r][c] == '#':
        F1[r][c] = -inf
        F2[r][c] = -inf
        return -inf

    # if it can, it goes to down, up and right, and it calls recursively itself
    down = up = right = -inf
    if r + 1 < n and direction != 2:
        down = longest(L, F1, F2, (r + 1, c), 1)
    if r - 1 >= 0 and direction != 1:  
        up = longest(L, F1, F2, (r - 1, c), 2)
    if c + 1 < n:
        right = longest(L, F1, F2, (r, c + 1), 3)
    
    # it adds the longest distance from neighbour +1 to the arrays of answers
    if direction != 2:
        F1[r][c] = max(down, right) + 1
    if direction != 1:
        F2[r][c] = max(up, right) + 1

    # it returns the answer from the proper array
    if direction == 1:
        return F1[r][c]
    if direction == 2:
        return F2[r][c]
    if direction == 3:
        return max( F1[r][c], F2[r][c] )

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(maze, all_tests=True)

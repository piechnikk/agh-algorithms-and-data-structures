# Paweł Piechnik
# Najpierw przekształcam dane wejściowe do listy 1d gdzie zapisuje w którym miejscu ile ropy można zatankować. Później jadę w strone pola końcowego zapisując które plamy minąłem i kiedy skończy się paliwo to dodaje do zbiornika największą miniętą plamę. Zwracam ile razy tankowałem. Złożoność to O(n*m)
from zad8testy import runtests

def merge_stain(T, tab, p, s):
    rows = len(T)
    cols = len(T[0])
    r = s[0]
    c = s[1]
    if T[r][c] == 0:
        return
    tab[p] += T[r][c]
    T[r][c] = 0
    if r+1 < rows and T[r+1][c] != 0:
        merge_stain(T, tab, p, (r+1, c))
    if c+1 < cols and T[r][c+1] != 0:
        merge_stain(T, tab, p, (r, c+1))
    if r-1 >= 0 and T[r-1][c] != 0:
        merge_stain(T, tab, p, (r-1, c))
    if c-1 >= 0 and T[r][c-1] != 0:
        merge_stain(T, tab, p, (r, c-1))
    

def plan(T):
    n = len(T[0])

    # it converts 2d array to 1d array by merge each available stains into a single field stain
    tab = [0]*n
    for i in range(n):
        merge_stain(T, tab, i, (0, i))

    # it goes from 0 to n-1 and when there is no fuel in tank, it take the largest passed stain
    stops_count = 1
    fuel = tab[0]
    possible_stops = []
    for i in range(1, n):
        if fuel == 0:
            taken_stain = max(possible_stops)
            fuel += taken_stain
            possible_stops.remove(taken_stain)
            stops_count+=1
        if tab[i] != 0:
            possible_stops.append(tab[i])
        fuel-=1


    return stops_count


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )
# Paweł Piechnik
# Najpierw przerabiam dane wejściowe na jedną tablice tablic każdy element to [odległość od startu, koszt, najmniejszy koszt dostania się do tego pola nie wykorzystując wyjątku, najmniejszy koszt dostania się do tego pola z wykożystaniem wyjątku], sortuje tą tablice, i przechodzę po niej od początku i jeśli z pola na którym stoje da się dojść mniejszym kosztem do innego pola to aktualizuje tamto pole. Na końcu zwracam najniższy koszt z wykorzystaniem wyjątku dla "mety"
from zad9testy import runtests
inf = float('inf')

def min_cost( O, C, T, L ):
    n = len(O) + 2
    # [length_from_start, cost, lowest_cost_without_exception, lowest_cost_with_exception]
    tab = [[0, 0, 0, 0]]
    for i in range(n - 2):
        tab.append([O[i], C[i], inf, inf])
    tab.sort(key=lambda x : x[0])
    tab.append([L, 0, inf, inf])

    for i in range(n):
        j = i+1
        while j < n and tab[j][0] <= tab[i][0] + T:
            # no exception
            tab[j][2] = min(tab[j][2], tab[i][2] + tab[j][1])
            # was exception but not now
            tab[j][3] = min(tab[j][3], tab[i][3] + tab[j][1])
            j+=1
        while j < n and tab[j][0] <= tab[i][0] + T*2:
            # now is exception
            tab[j][3] = min(tab[j][3], tab[i][2] + tab[j][1])
            j+=1
    return tab[n-1][3]
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( min_cost, all_tests = True )

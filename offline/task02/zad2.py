# Paweł Piechnik
# Sortuje tablice i wybieram od największych obszarów dopóki są większe niż liczba dni czyli ilość stopionego śniegu, stosuje sortowanie kopcowe bo przy naprawianu kopców mam największe wartości z listy i moge je przerwać kiedy liczba dni jest większa od wartości nieposortowanych elementów. Złożoność to chyba O(nlogn)

from zad2testy import runtests


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def parent(i):
    return (i - 1) // 2


def heapify(tab, i, n):
    l = left(i)
    r = right(i)
    max_i = i
    if l < n and tab[l] > tab[max_i]:
        max_i = l
    if r < n and tab[r] > tab[max_i]:
        max_i = r
    if max_i != i:
        tab[i], tab[max_i] = tab[max_i], tab[i]
        heapify(tab, max_i, n)


def buildheap(tab):
    n = len(tab)
    for i in range(parent(n - 1), -1, -1):
        heapify(tab, i, n)


def snow(S: list):
    n = len(S)

    buildheap(S)
    snow_collected = 0
    days_passed = 0
    for i in range(n - 1, 0, -1):
        S[0], S[i] = S[i], S[0]
        # zbieram największe obszary a kiedy już się nie opłaca to przerywam pętle i nie sortuje dalej
        if S[i] - days_passed > 0:
            snow_collected += S[i] - days_passed
            days_passed += 1
            heapify(S, 0, i)
        else:
            break
    return snow_collected


runtests(snow, all_tests=True)

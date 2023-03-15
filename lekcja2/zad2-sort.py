# zaimplementować scalanie list przez serie naturalną (domyślnie posortowane)

# merge(L1,L2)->L3 scalanie

# getns(L1)->L2 wycięcie serii naturalnej

# concat(L1,L2)->L przeniesienie na koniec

# empty(L1)->T/F


def sort(L):
    while not empty(L):
        L1 = getns(L)
        L2 = getns(L)
        new_list = merge(L1, L2)
        concat(L, new_list)

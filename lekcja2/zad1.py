# Dana jest posortowana tablica n elementow i liczba x czy istnieją i, j które dają sume
def find_indexes(T, x):  # różnica
    i, j = 0, 1
    while j < len(T) and T[j] - T[i] != x:
        if T[j] - T[i] < x:
            j += 1
        else:
            i += 1
    return i, j


def find_indexes2(T, x):  # suma
    i, j = 0, len(T) - 1
    while i != j or T[j] + T[i] != x:
        if T[i] + T[j] > x:
            j -= 1
        elif T[i] + T[j] < x:
            i += 1
        else:
            return True
    return False

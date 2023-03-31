# Paweł Piechnik
# Przechodzę przez tablice tworząc kopie mini tablic które sprawdzam, i wyszukuję w nich k-te najmniejsze elementy które na końcu sumuje. Jeśli przesuwając się odpadnie element mniejszy od ostatnio znalezionego i przyłączy się też mniejszy (analogicznie dla większych) to nie wyszukuje, tylko dodaje ostatnią maksymalną wartość. złożoność to chyba O(np)

from kol1testy import runtests


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] >= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


# wybieram k-ty największy element z tablicy A
def select(A, k):
    n = len(A)
    A_copy = A.copy()
    p = 0
    r = n - 1
    actual_i = partition(A_copy, p, r)
    while True:
        if actual_i == k:
            return A_copy[k]
        elif actual_i > k:
            r = actual_i - 1
        else:
            p = actual_i + 1
        actual_i = partition(A_copy, p, r)


def ksum(T, k, p):
    n = len(T)
    sum = 0
    last_select = None
    for i in range(n - p + 1):
        if (
            last_select is None
            or T[i - 1] == last_select
            or (T[i - 1] > last_select and T[i + p - 1] < last_select)
            or (T[i - 1] < last_select and T[i + p - 1] > last_select)
        ):
            last_select = select(T[i : i + p], k - 1)
        sum += last_select
    return sum


runtests(ksum, all_tests=True)

# Na wejściu mamy posortowany ciąg liczb całkowitych A={a0,...,an-1} z zakresu od 0 do m-1. Liczby są parami różne. Co więcej n<m. Proszę podać algorytm który znajduje najmniejszą liczbę całkowitą, której nie ma w A.
def smallest(A):
    n = len(A)
    start = 0
    end = n
    while start != end:
        middle = start + (end - start) // 2
        if middle < A[middle]:
            end = middle
        else:
            start = middle + 1
    return start


print(smallest([0, 1, 2, 3, 4, 5, 6, 7, 9, 12]))

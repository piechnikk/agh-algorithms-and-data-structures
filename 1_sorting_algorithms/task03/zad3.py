# Paweł Piechnik
# Dodaje do wejściowej listy wszystkie jej słowa ale odwrócone (pomijając palindromy), potem sortuje tą liste i zwracam ile razy występowało najczęściej występujące słowo. Złożoność to chyba O(n+nlogn)
from zad3testy import runtests


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def parent(i):
    return (i - 1) // 2


def heapify(A, i, n):
    l = left(i)
    r = right(i)
    max_i = i
    if l < n and A[l] > A[max_i]:
        max_i = l
    if r < n and A[r] > A[max_i]:
        max_i = r
    if max_i != i:
        A[i], A[max_i] = A[max_i], A[i]
        heapify(A, max_i, n)


def buildheap(A):
    n = len(A)
    for i in range(parent(n - 1), -1, -1):
        heapify(A, i, n)


def heapsort(A):
    n = len(A)
    buildheap(A)
    for i in range(n - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapify(A, 0, i)


def strong_string(T: list):
    for i in range(len(T)):
        if T[i] != T[i][::-1]:
            T.append(T[i][::-1])
    heapsort(T)
    max_strong = 0
    actual_word = T[0]
    actual_strong = 1
    for i in range(1, len(T)):
        if T[i] == actual_word:
            actual_strong += 1
        else:
            if actual_strong > max_strong:
                max_strong = actual_strong
            actual_word = T[i]
            actual_strong = 1
    return max_strong


# # zmien all_tests na True zeby uruchomic wszystkie testy
runtests(strong_string, all_tests=True)

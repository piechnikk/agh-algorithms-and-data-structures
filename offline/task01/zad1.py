# Paweł Piechnik
# Sprawdzam każdy palindrom od środka. Przyjmuje że każda litera pomijając pierwszą i ostatnią może być tym palindromem (środkową literą) i rozszerzam w obie strony dopóki nowe litery są takie same oraz nie wyjdę poza tablice.

from zad1testy import runtests


def ceasar(s):
    n = len(s)
    longest = 1
    for i in range(1, n - 2):
        prev_i = i - 1
        next_i = i + 1
        actual_length = 1
        while prev_i >= 0 and next_i <= n - 1 and s[prev_i] == s[next_i]:
            prev_i -= 1
            next_i += 1
            actual_length += 2
        if actual_length > longest:
            longest = actual_length
            # przyśpieszenie w przypadku kiedy cały ciąg to palindrom
            if longest == n + ((n % 2) - 1):
                break

    return longest


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(ceasar, all_tests=True)

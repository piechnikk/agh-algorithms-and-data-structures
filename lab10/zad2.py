# mamy kwote i zbior nominalow monet C
# wydaj kwote T minimalna liczba monet

# np T = 15
# C = {1, 5, 8}
# podejscie zachlanne: monety 8 -> 5 -> 1 -> 1 (4 monety, bierzermy od najwiekszych nominalow jesli jest to mozliwe)
# podejscie optymalne: monety 5 -> 5 -> 5 (3 monety, dowod ze model zachlanny nie dziala)

# funkcja f(T) = min([f(T - nominal) + 1 for nominal in C]) - dla kazdego nominalu odpalamy f(T - nominal) i wybieramy najmniejsze
# f(T) - zwraca minimalna liczbe monet niezbedna do wydania kwoty T
# f(0) = 0
# f(T) = inf, dla T < 0

# implementacja:
def change(T, C):
    coins = [float("inf")] * (T + 1)
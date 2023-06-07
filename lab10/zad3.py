# mamy przykladowy ciag, np
# A = 0, 7, 3, 0, 2, 9
# i kolejny, np 
# B = 3, 5, 1, 0, 7, 9, 11

# szukamy najdluzszego wspolnego podciagu:
# rozwiazanie to 3, 0, 9 (z A "wykresla" 0, 7, 2, z B "wykresla" 5, 1, 7, 11)

# A - ciag rozmiaru n
# B - ciag rozmiaru m

# f(i, j) - najdluzszy wspolny podciag ciagow A[1..i] oraz B[1..j]
# f(0, j) = 0
# f(i, 0) = 0
# f(i, j) = {
#               f(i - 1, j - 1) + 1, gdy A[i] == B[j],
#               max(f(i - 1, j), f(i, j - 1)), gdy A[i] != B[j],
#               0, gdy i == 0 lub j == 0
# }

# warto zrobic rekurencje ze spamietywaniem lub tablice 2D w ktorej bedziemy pamietac wyniki
# w przeciwnym przypadku algorytm robi sie wykladniczy
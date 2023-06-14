# ciag od A_0 do A_(n-1)
# chcemy go podzielic na dokladnie k podciagow spojnych
# oraz zeby najwieksza suma elementow w kazdym podciagu spojnym byla mozliwie najmniejsza

# np:
# 0, 3, 7, 8, 12, 3, 4, -5
# fragmenty: (0, 3, 7, 8), (12, 3), (4, -5)
#             suma 18       suma 15  suma -1, a wiec koszt to 18 (najwieksza z sum)
# fragmenty: (0, 3, 7), (8, 12, 3), (4, -5)
#             suma 10    suma 23     suma -1, a wiec koszt to 23


# A - ciag wejsciowy
# f(i, j, m) - najwieksza suma fragmentu w optymalnym (zgodnym z warunkami zadania) podziale
#               ciagu A od indeksu i do indeksu j na m fragmentow


# PD - zakodowac zad 4 w n logn
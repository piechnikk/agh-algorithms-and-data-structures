import numpy

# def anagram(a, b):
#     z_code = ord("z")
#     a_code = ord("a")
#     len_a = len(a)
#     len_b = len(b)
#     if len_a != len_b:
#         return False
#     A = [0 for _ in range(z_code - a_code)]
#     B = [0 for _ in range(z_code - a_code)]
#     for i in range(len_a):
#         A[ord(a[i]) - a_code] += 1
#         B[ord(b[i]) - a_code] += 1
#     return A == B

C = numpy.empty(2 ^ 21)


def anagram(a, b):
    z_code = ord("z")
    a_code = ord("a")
    len_a = len(a)
    len_b = len(b)
    if len_a != len_b:
        return False
    for i in range(len_a):
        C[ord(a[i])] = 0
        C[ord(b[i])] = 0
    for i in range(len_a):
        C[ord(a[i])] += 1
        C[ord(b[i])] -= 1

    for i in range(len_a):
        if C[ord(a[i])] != 0:
            return False
    return True


# najprościej posortować i porównać

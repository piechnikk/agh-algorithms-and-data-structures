# it runs counting sort from the end, first the last letter to the first, and we have sorted alphabetically
# complexity O(nt) -> n - number of words, t - length of the longest word
K = ord("z") - ord("a") + 1
START = ord("a")


def countingsort(A: list[str], possition: int):
    K = ord("z") - ord("a") + 1
    START = ord("a")

    n = len(A)
    C = [0] * K
    B = [0] * n
    print(A)
    for i in range(n):
        current_letter = ord(A[i][possition]) - START if len(A[i]) > possition else 0
        C[current_letter] += 1
    for i in range(1, K):
        C[i] += C[i - 1]
    for i in range(n - 1, -1, -1):
        current_letter = ord(A[i][possition]) - START if len(A[i]) > possition else 0
        C[current_letter] -= 1
        B[C[current_letter]] = A[i]
    for i in range(n):
        A[i] = B[i]


def sort(A):
    n = len(A)
    max_length = 0
    for i in range(n):
        word_len = len(A[i])
        if word_len > max_length:
            max_length = word_len
    for i in range(max_length - 1, -1, -1):
        countingsort(A, i)


A = ["pies", "ada", "adb", "asd", "ajdskaldjksljdkl"]
sort(A)
print(A)

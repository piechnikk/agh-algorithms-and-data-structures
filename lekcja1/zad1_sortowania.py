# sortowanie przez wstawianie
def insertion_sort(tab):
    l = len(tab)
    for i in range(l):
        for j in range(i, 0):
            if tab[j - 1] < tab[j]:
                tab[j - 1], tab[j] = tab[j], tab[j - 1]


class Node:
    def __init__(self, v: int, next=None):
        self.v: int = v
        self.next: Node = next


# wstawiamy do listy posortowanej rosnąco
def l_insert(head: Node, n: Node):
    p = head
    while p.next is not None and p.next.v < n:
        p = p.next
    n.next = p.next
    p.next = n
    return head


# usuwamy maksimum z dowolnej listy
def remove_max(head: Node):
    m = head.next.v
    mptr = head
    p = mptr.next
    while p.next is not None:
        if p.next.v > m:
            mptr = p
            m = p.next.v
        p = p.next
    ret = mptr.next
    mptr.next = mptr.next.next
    return ret


def isort(head: Node):
    sorted = Node(None)
    while head.next is not None:
        p = head.next
        head.next = head.next.next
        p.next = None
        sorted = l_insert(sorted, p)
    return sorted


# znajdź minimum i maksimum z listy o n elementach wykorzystując tylko 3/2 n porównań
def find_min_max(T: list):
    minimum = makssimum = T[0]
    for i in range(0, len(T), 2):
        if T[i] < T[i + 1]:
            if T[i] < minimum:
                minimum = T[i]
            if T[i + 1] > maksimum:
                maksimum = T[i + 1]
        else:
            if T[i + 1] < minimum:
                minimum = T[i + 1]
            if T[i] > maksimum:
                maksimum = T[i]


# szukamy 2 indeksów ij tż T[i]-T[j]=6
T = [1, 4, 5, 8, 9, 10, 12]


def find_indexes(T):
    j, i = 0, 1
    while i < len(T) and T[i] - T[j] != 6:
        if T[i] - T[j] < 6:
            i += 1
        else:
            j += 1
    return i, j


print(find_indexes(T))

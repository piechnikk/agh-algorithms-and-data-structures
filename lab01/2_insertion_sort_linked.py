# class for linked list
class Node:
    def __init__(self, val: int, next=None):
        self.val: int = val
        self.next: Node = next


# insertion into an ascending sorted linked list
def l_insert(head: Node, n: Node):
    p = head
    while p.next is not None and p.next.val < n:
        p = p.next
    n.next = p.next
    p.next = n
    return head


# insertion sort in linked list
def isort(head: Node):
    sorted = Node(None)
    while head.next is not None:
        p = head.next
        head.next = head.next.next
        p.next = None
        sorted = l_insert(sorted, p)
    return sorted

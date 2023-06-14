# class for linked list
class Node:
    def __init__(self, val: int, next=None):
        self.val: int = val
        self.next: Node = next


# delete maximum value from linked list
def remove_max(head: Node):
    max_val = head.next.val
    max_prev = head
    max_node = max_prev.next
    while max_node.next is not None:
        if max_node.next.val > max_val:
            max_prev = max_node
            max_val = max_node.next.val
        max_node = max_node.next
    deleted_value = max_prev.next
    max_prev.next = max_prev.next.next
    return deleted_value

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def merge_missions(mission1, mission2):
    if mission1 is None:
        return mission2
    if mission2 is None:
        return mission1

    if mission1.value <= mission2.value:
        mission1.next = merge_missions(mission1.next, mission2)
        return mission1
    else:
        mission2.next = merge_missions(mission1, mission2.next)
        return mission2

def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

# mission1 = Node(1, Node(2, Node(4)))
# mission2 = Node(1, Node(3, Node(4, Node(5))))
mission1 = None
mission2 = None

merged_head = merge_missions(mission1, mission2)
print_linked_list(merged_head)




'''
All the clues that lead us in circles are false evidence we need to purge! Given the head of a linked list evidence, clean up the evidence list by identifying any false clues. Write a function collect_false_evidence() that returns an array containing all values that are part of any cycle in evidence. Return the values in any order.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
'''
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def collect_false_evidence(evidence):
    visited = set()
    cycle = set()
    current = evidence
    while current:
        if current in visited:
            break
        visited.add(current)
        current = current.next
    
    if current: 
        start = current
        while current not in cycle:
            cycle.add(current)
            current = current.next
            if current == start:
                break
    return [node.value for node in cycle]

clue1 = Node("Unmarked sedan seen near the crime scene")
clue2 = Node("The stolen goods are at an abandoned warehouse")
clue3 = Node("The mayor is accepting bribes")
clue4 = Node("They dumped their disguise in the lake")
clue1.next = clue2
clue2.next = clue3
clue3.next = clue4
clue4.next = clue2

clue5 = Node("A masked figure was seen fleeing the scene")
clue6 = Node("Footprints lead to the nearby woods")
clue7 = Node("A broken window was found at the back")
clue5.next = clue6
clue6.next = clue7

print(collect_false_evidence(clue1))
print(collect_false_evidence(clue5))
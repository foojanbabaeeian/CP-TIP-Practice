'''
Problem 1: Linked List Game
As the judge of the game show, you are given the head of a linked list of even length containing integers.

Each odd-indexed node contains an odd integer and each even-indexed node contains an even integer.

We call each even-indexed node and its next node a pair, e.g., the nodes with indices 0 and 1 are a pair, the nodes with indices 2 and 3 are a pair, and so on.

For every pair, we compare the values of the nodes in the pair:

If the odd-indexed node is higher, the "Odd" team gets a point.
If the even-indexed node is higher, the "Even" team gets a point.
Write a function game_result() that returns the name of the team with the higher points, if the points are equal, return "Tie".

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# For testing
def print_linked_list(head):
	current = head
	while current:
		print(current.value, end=" -> " if current.next else "\n")
		current = current.next

def game_result(head):
    pass
Example Usage:

game1 = Node(2, Node(1))
game2 = Node(2, Node(5, Node(4, Node(7, Node(20, Node(5))))))
game3 = Node(4, Node(5, Node(2, Node(1))))

print(game_result(game1))
print(game_result(game2))
Example Output:

Even
Example 1 Explanation: There is only one pair in this linked list and that is (2,1).
Since 2 > 1, the Even team gets the point.
Hence, the answer is "Even".

Odd
Example 2 Explanation: There are 3 pairs in this linked list. 
Let's investigate each pair individually:
(2,5) -> Since 2 < 5, The Odd team gets the point.
(4,7) -> Since 4 < 7, The Odd team gets the point.
(20,5) -> Since 20 > 5, The Even team gets the point.
The Odd team earned 2 points while the Even team got 1 point and the Odd team has the higher points.
Hence, the answer is "Odd".

Tie
Example 3 Explanation: There are 2 pairs in this linked list. 
Let's investigate each pair individually:
(4,5) -> Since 4 < 5, the Odd team gets the point.
(2,1) -> Since 2 > 1, the Even team gets the point.
Both teams earned 1 point.
Hence, the answer is "Tie".'''


# class Node:
# 	def __init__(self, value, next=None):
# 		self.value = value
# 		self.next = next

# # For testing
# def print_linked_list(head):
# 	current = head
# 	while current:
# 		print(current.value, end=" -> " if current.next else "\n")
# 		current = current.next

# def game_result(head):
#     pass

# game1 = Node(2, Node(1))
# game2 = Node(2, Node(5, Node(4, Node(7, Node(20, Node(5))))))
# game3 = Node(4, Node(5, Node(2, Node(1))))

# print(game_result(game1))
# print(game_result(game2))

'''
Problem 2: Cycle Start
On your marks, get set, go! Contestants in the game show are racing along a path that contains a loop, but there's a hidden mini challenge: they aren't told where along the path the loop begins. Given the head of a linked list, path_start where each node represents a point in the path, return the value of the node at the start of the loop. If no loop exists in the path, return None.

A linked list has a cycle or loop if at some point in the list, the node’s next pointer points back to a previous node in the list.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def cycle_start(path_start):
	pass
Example Usage:

Linked list with 4 nodes and a cycle where 4th node points to 2nd node

path_start = Node('Start', Node('Point 1', Node('Point 2', Node('Point 3'))))
path_start.next.next.next.next = path_start.next
print(cycle_start(path_start))
Example Output:

Point 1
'''


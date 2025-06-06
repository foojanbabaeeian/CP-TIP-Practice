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

'''
Problem 1: Next in Queue
Each user on a music app should have a queue of songs to play next. Implement the class Queue using a singly linked list. Recall that a queue is a First-In-First-Out (FIfO) data structure where elements are added to the end (the tail) and removed from the front (the head).

Your queue must have the following methods:

__init()__: Initializes an empty queue (provided)
enqueue(): Accepts a tuple of two strings (song, artist) and adds the element with the specified tuple to the end of the queue.
dequeue(): Removes and returns the element at the front of the queue. If the queue is empty, returns None.
peek(): Returns the value of the element at the front of the queue without removing it. If the queue is empty, returns None.
is_empty(): Returns True if the queue is empty, and False otherwise.
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# For testing
def print_queue(head):
    current = head.front
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def is_empty(self):
        pass

    def enqueue(self):
        pass
    
    def dequeue(self):
        pass
    
    def peek(self):
        pass
    
Example Usage:

# Create a new Queue
q = Queue()

# Add elements to the queue
q.enqueue(('Love Song', 'Sara Bareilles'))
q.enqueue(('Ballad of Big Nothing', 'Elliot Smith'))
q.enqueue(('Hug from a Dinosaur', 'Torres'))
print_queue(q)

# View the front element
print("Peek: ", q.peek()) 

# Remove elements from the queue
print("Dequeue: ", q.dequeue()) 
print("Dequeue: ", q.dequeue()) 

# Check if the queue is empty
print("Is Empty: ", q.is_empty()) 

# Remove the last element
print("Dequeue: ", q.dequeue()) 

# Check if the queue is empty
print("Is Empty:", q.is_empty()) 
Example Output:

('Love Song', 'Sara Bareilles') -> ('Ballad of Big Nothing', 'Elliot Smith') 
-> ('Hug from a Dinosaur', 'Torres')
Peek:  ('Love Song', 'Sara Bareilles')
Dequeue:  ('Love Song', 'Sara Bareilles')
Dequeue:  ('Ballad of Big Nothing', 'Elliot Smith')
Is Empty:  False
Dequeue:  ('Hug from a Dinosaur', 'Torres')
Is Empty: True

'''

def problem1():
	class Node:
		def __init__(self, value, next=None):
			self.value = value
			self.next = next

	# For testing
	def print_queue(head):
		current = head.front
		while current:
			print(current.value, end=" -> " if current.next else "")
			current = current.next
		print()

	class Queue:
		def __init__(self):
			self.front = None
			self.rear = None
		
		def is_empty(self):
			return self.front is None

		def enqueue(self, val):
			if not self.front:
				self.front = Node(val)
				self.rear = self.front
				return
			
			self.rear.next = Node(val)
			self.rear = self.rear.next
		
		def dequeue(self):
			if self.front:
				temp = self.front
				self.front = self.front.next
				return temp.value
			return None
		
		def peek(self):
			if self.front:
				return self.front.value
			return None
		
	# Create a new Queue
	q = Queue()

	# Add elements to the queue
	q.enqueue(('Love Song', 'Sara Bareilles'))
	q.enqueue(('Ballad of Big Nothing', 'Elliot Smith'))
	q.enqueue(('Hug from a Dinosaur', 'Torres'))
	print_queue(q)

	# View the front element
	print("Peek: ", q.peek()) 

	# Remove elements from the queue
	print("Dequeue: ", q.dequeue()) 
	print("Dequeue: ", q.dequeue()) 

	# Check if the queue is empty
	print("Is Empty: ", q.is_empty()) 

	# Remove the last element
	print("Dequeue: ", q.dequeue()) 

	# Check if the queue is empty
	print("Is Empty:", q.is_empty()) 


'''

Problem 2: Merge Playlists
You are given the head of two linked lists, playlist1 and playlist2 with lengths n and m respectively. Remove playlist1's nodes from the ath to the bth node and put playlist2 in its place. Assume the lists are 0-indexed.

The blue edges and nodes in the figure below indicate the result:

Merged playlists

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

def merge_playlists(playlist1, playlist2, a, b):
    pass
Example Usage:

playlist1 = Node(('Flea', 'St. Vincent'),
                Node(('Juice', 'Lizzo'), 
                    Node(('Tenderness', 'Jay Som'),
                        Node(('Ego Death', 'The Internet'),
                            Node(('Empty', 'Kevin Abstract'))))))

playlist2 = Node(('Dreams', 'Solange'), Node(('First', 'Gallant')))

print_linked_list(merge_playlists(playlist1, playlist2, 2, 3))
Example Output:

('Flea', 'St.Vincent') -> ('Juice', 'Lizzo') -> ('Dreams', 'Solange') -> ('First', 'Gallant')
-> ('Empty', 'Kevin Abstract')
'''

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

def merge_playlists(playlist1, playlist2, a, b):
	# 1 -> 2 -> 3      4   -> 5
				# 3 -> 4 
	# boo -> baa -> bee

	# 1 -> 2 -> boo -> baa -> bee -> 5
	
	current = playlist1
	playlist2_head = playlist2
	for _ in range(a - 1):
		current = current.next
	playlist1_head = current.next
	current.next = playlist2_head
	# print("checking playlistt 1 and current", playlist1_head.value, current.value)
	while playlist2_head.next:
		playlist2_head = playlist2_head.next
	print("checking playlistt 2", playlist2_head.value)

	for _ in range(b - a + 1):
		playlist1_head = playlist1_head.next

	print("checking playlistt 1", playlist1_head.value)

	playlist2_head.next = playlist1_head

	return playlist1

playlist1 = Node(('Flea', 'St. Vincent'),
                Node(('Juice', 'Lizzo'), 
                    Node(('Tenderness', 'Jay Som'),
                        Node(('Ego Death', 'The Internet'),
                            Node(('Empty', 'Kevin Abstract'))))))

playlist2 = Node(('Dreams', 'Solange'), Node(('First', 'Gallant')))

print_linked_list(merge_playlists(playlist1, playlist2, 2, 3))
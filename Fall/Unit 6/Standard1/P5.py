# Problem 5: Looped
# Given the head of a linked list playlist_head that may contain a cycle, use the fast and slow pointer method to return the length of the cycle. If the list does not contain a cycle, return 0.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

class SongNode:
	def __init__(self, song, artist, next=None):
		self.song = song
		self.artist = artist
		self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()

def loop_length(playlist_head):
	point1 = playlist_head
	point2 = playlist_head
	
	while point2 and point2.next:
		point1 = point1.next
		point2 = point2.next.next
		if point2 == point1:
			count = 0
			current = point1
			while True:
				current = current.next 
				count +=1
				if current == point1:
					break
			return count
	return 0
			
			
	

'''
if slow == fast: # Now, calculate the cycle length cycle_length = 0 current = slow while True: current = current.next cycle_length += 1 if current == slow: break return cycle_length # No cycle found return 0
'''
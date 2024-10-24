# Problem 4: On Repeat
# A variation of the two-pointer technique introduced in previous units is to have a slow and a fast pointer that increment at different rates.

# We would like to check whether our playlist loops or not. Given the head of a linked list playlist_head, return True if the playlist has a cycle in it and False otherwise. A linked list has a cycle if at some point in the list, the node’s next pointer points back to a previous node in the list.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

class SongNode:
	def __init__(self, song, artist, next=None):
		self.song = song
		self.artist = artist
		self.next = next

def on_repeat(playlist_head):
	point1 = playlist_head
	point2 = playlist_head
	while point2 and point2.next:
		point1 = point1.next
		point2 = point2.next.next
		if point1 == point2:
			return True
	return False
	


song1 = SongNode("GO!", "Common")
song2 = SongNode("N95", "Kendrick Lamar")
song3 = SongNode("WIN", "Jay Rock")
song4 = SongNode("ATM", "J. Cole")
song1.next = song2
song2.next = song3
song3.next = song4
song4.next = song1

print(on_repeat(song1))
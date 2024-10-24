# Problem 2: Top Artists
# Given the head of a linked list playlist, return a dictionary that maps each artist in the list to its frequency.

# Evaluate the time complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

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


def get_artist_frequency(playlist):
	artist_num = {}
	current = playlist
	while current:
		artist = current.artist
		if artist in artist_num:
			artist_num[artist] +=1
		else:
			artist_num[artist] = 1
		current = current.next
	return artist_num
# Example Usage:

playlist = SongNode("Saturn", "SZA", 
                SongNode("Who", "Jimin", 
                        SongNode("Espresso", "Sabrina Carpenter", 
                                SongNode("Snooze", "SZA"))))

print(get_artist_frequency(playlist))
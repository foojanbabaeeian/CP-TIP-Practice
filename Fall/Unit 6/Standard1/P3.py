# Problem 3: Glitching Out
# The following code attempts to remove the first node with a given song from a singly linked list with head playlist_head but it contains a bug!

# Step 1: Copy this code into Replit.

# Step 2: Create your own test cases to run the code against, and use print statements and the stack trace to identify and fix the bug so that the function correctly removes a node by value from the list.

# Step 3: Evaluate the time and space complexity of the fixed solution. Define your variables and provide a rationale for why you believe the solution has the stated time and space complexity.


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


# Function with a bug!
def remove_song(playlist_head, song):
    if not playlist_head:
        return None
    if playlist_head.song == song:
        return playlist_head.next

    current = playlist_head
    while current.next:
        if current.next.song == song:
            current.next = current.next.next  
            return playlist_head 
        current = current.next

    return playlist_head

# playlist = SongNode("SOS", "ABBA", SongNode("Simple Twist of Fate", "Bob Dylan"),SongNode("Dreams", "Fleetwood Mac",SongNode("Lovely Day", "Bill Withers")))

node1 = SongNode("Lovely Day", "Bill Withers")
node2 = SongNode("Dreams", "Fleetwood Mac", node1)
node3 = SongNode("Simple Twist of Fate", "Bob Dylan", node2)
playlist = SongNode("SOS", "ABBA", node3)
print_linked_list(remove_song(playlist, "Dreams"))
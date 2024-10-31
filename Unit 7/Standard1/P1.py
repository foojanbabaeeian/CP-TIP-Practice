'''
Problem 1: Counting Iron Man's Suits
Tony Stark, aka Iron Man, has designed many different suits over the years. Given a list of strings suits where each string is a suit in Stark's collection, count the total number of suits in the list.

Implement the solution iteratively without the use of the len() function.
Implement the solution recursively.
Discuss: what are the similarities between the two solutions? What are the differences?
def count_suits_iterative(suits):
    pass

def count_suits_recursive(suits):
    pass
Example Usage:

print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III", "Mark IV"]))
Example Output:

3
4
'''


def count_suits_iterative(suits):
    sum = 0
    for i in range(len(suits)):
        sum += 1
    return sum

def count_suits_recursive(suits):
    # base case 
    # list is empty -> return 0
    if not suits:
        return 0
    return 1 + count_suits_iterative(suits[1:])

print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III", "Mark IV"]))
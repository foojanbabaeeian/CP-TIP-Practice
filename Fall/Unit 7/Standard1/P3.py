'''
Problem 3: Counting Unique Suits
Some of Iron Man's suits are duplicates. Given a list of strings suits where each string is a suit in Stark's collection, count the total number of unique suits in the list.

Implement the solution iteratively.
Implement the solution recursively.
Discuss: what are the similarities between the two solutions? What are the differences?
Evaluate the time complexity of each solution. Are they the same? Define your variables and provide a rationale for why you believe your solution has the stated time complexity.
def count_suits_iterative(suits):
    pass

def count_suits_recursive(suits):
    pass
Example Usage:

print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III"]))

Example Output:

3
2
'''

# def count_suits_iterative(suits):
#     sum = 0
#     check = []
#     for i in range(len(suits)):
#         if suits[i] not in check:
#             sum +=1
#             check.append(suits[i])
#     return sum


def count_suits_iterative(suits):
    # sum = 0
    check = set(suits)
    # for i in range(len(check)):
    #     sum += 1
    return len(check)

# Base case: if the list is empty
# Return the count of unique suits
# Add the first suit to the set
# Recurse with the rest of the list
check = []
def count_suits_recursive(suits):
    if not suits:
        return 0
    # if suits[0] not in suits:
    #     return 1 + count_suits_iterative(suits[1:])
    first = suits[0]
    if first in suits[1:]:
        print(first, suits)
        return count_suits_recursive(suits[1:])
    else:
        print("else" ,first, suits)
        return 1+ count_suits_recursive(suits[1:])

# For the iterative solution, use a set to collect unique suits and return its length.
# For the recursive solution, compare each suit with the rest of the list and count only those that are unique.

print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III"]))
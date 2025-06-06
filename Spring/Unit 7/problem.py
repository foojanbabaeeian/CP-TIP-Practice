'''
Problem 1: Counting the Layers of a Sandwich
You're working at a deli, and need to count the layers of a sandwich to make sure you made the order correctly. Each layer is represented by a nested list. Given a list of lists sandwich where each list [] represents a sandwich layer, write a recursive function count_layers() that returns the total number of sandwich layers.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def count_layers(sandwich):
    pass
Example Usage:

sandwich1 = ["bread", ["lettuce", ["tomato", ["bread"]]]]
sandwich2 = ["bread", ["cheese", ["ham", ["mustard", ["bread"]]]]]

print(count_layers(sandwich1))
print(count_layers(sandwich2))
Example Output:

4
5
'''

# def count_layers(sandwich):
# 	cnt = 0
# 	if len(sandwich) == 0:
# 		return cnt
# 	else:
# 		sandwich[:] = sandwich[-1]
# 		cnt += 1
# 		count_layers(sandwich)
		
# 	return cnt

def prop1():
    def count_layers(sandwich):
        if len(sandwich) == 1: #base case
            return 1
        else: 
            return 1+ count_layers(sandwich[-1])
    sandwich1 = ["bread", ["lettuce", ["tomato", ["bread"]]]]
    sandwich2 = ["bread", ["cheese", ["ham", ["mustard", ["bread"]]]]]
    print(count_layers(sandwich1))
    print(count_layers(sandwich2))


'''
Problem 2: Reversing Deli Orders
The deli counter is busy, and orders have piled up. To serve the last customer first, you need to reverse the order of the deli orders. Given a string orders where each individual order is separated by a single space, write a recursive function reverse_orders() that returns a new string with the orders reversed.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def reverse_orders(orders):
    pass
Example Usage:

print(reverse_orders("Bagel Sandwich Coffee"))
Example Output:

Coffee Sandwich Bagel
'''
def prob2():
    def make_list(orders):
        return orders.split(" ")

    def reverse_orders(orders):
        # if len(orders) == 0:
        #     return orders
        # else:
        #     return reverse_orders(orders[1:]) + " " + orders[0]
        if len(make_list(orders)) == 1:
            return orders
        else:
            return reverse_orders(" ".join(make_list(orders)[1:])) + " " + make_list(orders[0])
    print(reverse_orders("Bagel Sandwich Coffee"))


# def reverse_orders(orders):
#     if len(orders) == 0:
#         return orders
#     else:
#         return reverse_orders(orders[1:]) + " " + orders[0]
'''
Problem 3: Sharing the Coffee
The deli staff is in desperate need of caffeine to keep them going through their shift and has decided to divide the coffee supply equally among themselves. Each batch of coffee is stored in containers of different sizes. Write a recursive function can_split_coffee() that accepts a list of integers coffee representing the volume of each batch of coffee and returns True if the coffee can be split evenly by volume among n staff and False otherwise.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def can_split_coffee(coffee, n):
pass
Example Usage:

print(can_split_coffee([4, 4, 8], 2))
print(can_split_coffee([5, 10, 15], 4))
Example Output:

True
False
'''
def prop3():
    def can_split_coffee(coffee, n):
        if len(coffee) == 0:
            return True
        if len(coffee) == 1:
            return coffee[0] % n == 0
        if coffee.pop() % n != 0:
            return False
        return can_split_coffee(coffee, n)
        
    print(can_split_coffee([4, 4, 8], 2))
    print(can_split_coffee([5, 10, 15], 4))

'''
Problem 4: Super Sandwich
A regular at the deli has requested a new order made by merging two different sandwiches on the menu together. Given the heads of two linked lists sandwich_a and sandwich_b where each node in the lists contains a spell segment, write a recursive function merge_orders() that merges the two sandwiches together in the pattern:

a1 -> b1 -> a2 -> b2 -> a3 -> b3 -> ...

Return the head of the merged sandwich.

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

def merge_orders(sandwich_a, sandwich_b)
    pass
Example Usage:

sandwich_a = Node('Bacon', Node('Lettuce', Node('Tomato')))
sandwich_b = Node('Turkey', Node('Cheese', Node('Mayo')))
sandwich_c = Node('Bread')

print_linked_list(merge_orders(sandwich_a, sandwich_b))
print_linked_list(merge_orders(sandwich_a, sandwich_c))
Example Output:

Bacon -> Turkey -> Lettuce -> Cheese -> Tomato -> Mayo
Bacon -> Bread -> Lettuce -> Tomato
'''



# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# def merge_orders(sandwich_a, sandwich_b):
#     if sandwich_a is None and sandwich_b is None:
#         return sandwich_b or sandwich_a

def find_frequency_positions(transmissions, target_code):
    def find_first():
        left, right = 0, len(transmissions) - 1
        first = -1
        while left <= right:
            mid = (left + right) // 2
            if transmissions[mid] < target_code:
                left = mid + 1
            elif transmissions[mid] > target_code:
                right = mid - 1
            else:
                first = mid
                right = mid - 1  
        return first

    def find_last():
        left, right = 0, len(transmissions) - 1
        last = -1
        while left <= right:
            mid = (left + right) // 2
            if transmissions[mid] < target_code:
                left = mid + 1
            elif transmissions[mid] > target_code:
                right = mid - 1
            else:
                last = mid
                left = mid + 1  
        return last

    first = find_first()
    if first == -1:
        return (-1, -1)
    last = find_last()
    return (first, last)
print(find_frequency_positions([5,7,7,8,8,10], 8))
print(find_frequency_positions([5,7,7,8,8,10], 6))
print(find_frequency_positions([], 0))
'''
Problem 6: Supply Chain
In the sustainable fashion industry, managing the supply chain efficiently is crucial. Supplies arrive in a sequence, and you need to process them in the order they arrive. However, some supplies may be of higher priority due to their eco-friendliness or scarcity.

Write the process_supplies() function, which takes a list of supplies (each with a name and a priority level) and returns a list of supply names in the order they would be processed, with higher priority supplies processed first.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def process_supplies(supplies):
    pass
Example Usage:

supplies = [("Organic Cotton", 3), ("Recycled Polyester", 2), ("Bamboo", 4), ("Hemp", 1)]
supplies_2 = [("Linen", 2), ("Recycled Wool", 5), ("Tencel", 3), ("Organic Cotton", 4)]
supplies_3 = [("Linen", 3), ("Hemp", 2), ("Recycled Polyester", 5), ("Bamboo", 1)]

print(process_supplies(supplies))
print(process_supplies(supplies_2))
print(process_supplies(supplies_3))
Example Output:

['Bamboo', 'Organic Cotton', 'Recycled Polyester', 'Hemp']
['Recycled Wool', 'Organic Cotton', 'Tencel', 'Linen']
['Recycled Polyester', 'Linen', 'Hemp', 'Bamboo']
'''
import heapq

# def process_supplies(supplies):

def process_supplies(supplies):
    '''
    [3, 2,  4,  1]
    the name of the products 
    in a order of 
    [4, 3, 2, 1]
    '''
    # Time complexity is O(n log n)

    dictionary_of_items = {}
    for supply in supplies:
        dictionary_of_items[supply[1]] = supply[0]    

    list_dictionary = list(dictionary_of_items.keys())
    list_dictionary.sort(reverse= True)
    result = [] 
    # print(list_dictionary)
    for element in list_dictionary: 
        result.append(dictionary_of_items[element]) #here i am adding the names associated to those specific numbers to the final list
    return result




# supplies = [("Organic Cotton", 3), ("Recycled Polyester", 2), ("Bamboo", 4), ("Hemp", 1)]
# supplies_2 = [("Linen", 2), ("Recycled Wool", 5), ("Tencel", 3), ("Organic Cotton", 4)]
# supplies_3 = [("Linen", 3), ("Hemp", 2), ("Recycled Polyester", 5), ("Bamboo", 1)]

# print(process_supplies(supplies))
# print(process_supplies(supplies_2))
# print(process_supplies(supplies_3))
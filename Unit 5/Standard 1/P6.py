'''
Problem 6: Print Inventory
Update the Villager class with a method print_inventory() that accepts no parameters except for self.

The method should print the name and quantity of each item in a villager’s furniture list.

The name and quantity should be in the format "item1: quantity, item2: quantity, item3: quantity" for however many unique items exist in the villager's furniture list
If the player has no items, the function should print "Inventory empty".
class Villager():
    # ... methods from previous problems
    
    def print_inventory(self):
        # Implement the method here
        pass
Example Usage:

alice = Villager("Alice", "Koala", "guvnor")

alice.print_inventory()

alice.items = ["acoustic guitar", "ironwood kitchenette", "kotatsu", "kotatsu"]
alice.print_inventory()
Example Output:

Inventory empty
acoustic guitar: 1, ironwood kitchenette: 1, kotatsu: 2
'''
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.__catchphrase = catchphrase
        self.furniture = []
    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.__catchphrase}!"
    def set_catchphrase(self, new_catchphrase):
        self.__catchphrase = new_catchphrase
    
    def add_item(self, item_name):
        self.furniture.append(item_name)
    def print_inventory(self):
        # Implement the method here
        inventory = {}
        if len(self.furniture) == 0:
            print("Inventory empty")
        for i in self.furniture:
            if i not in inventory:
                inventory[i] = 1
            else:
                inventory[i] +=1
        for key, val in inventory.items():
            print(key, ":", val, end=", ")
alice = Villager("Alice", "Koala", "guvnor")

alice.print_inventory()

alice.furniture = ["acoustic guitar", "ironwood kitchenette", "kotatsu", "kotatsu"]
alice.print_inventory()
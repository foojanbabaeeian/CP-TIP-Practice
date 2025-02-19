'''
Problem 7: Group by Personality
The Villager class has been updated below to include the new string attribute personality representing the character's personality type.

Outside of the Villager class, write a function of_personality_type(). Given a list of Villager instances townies and a string personality_type as parameters, return a list containing the names of all villagers in townies with personality personality_type. Return the names in any order.

class Villager:
    def __init__(self, name, species, personality, catchphrase):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
    # ... methods from previous problems
    
def of_personality_type(townies, personality_type):
    pass
Example Usage:

isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")

print(of_personality_type([isabelle, bob, stitches], "Lazy"))
print(of_personality_type([isabelle, bob, stitches], "Cranky"))
Example Output:

["Bob", "Stitches"]
[]
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
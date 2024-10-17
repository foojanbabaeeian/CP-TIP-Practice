'''
Step 1: Copy the following code into your IDE.

Step 2: Instantiate an instance of the class Villager, which represents characters in Animal Crossing. Store the instance in a variable named apollo.

The Villager object created should have the name "Apollo", the species "Eagle", and the catchphrase "pah".
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

# Instantiate your villager here
Example Usage:

print(apollo.name)  
print(apollo.species)  
print(apollo.catchphrase) 
print(apollo.furniture) 
Example Output:

Apollo
Eagle
pah
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
	
alice = Villager("Alice", "Koala", "guvnor")
print(alice.furniture)

alice.add_item("acoustic guitar")
print(alice.furniture)

alice.add_item("cacao tree")
print(alice.furniture)

alice.add_item("nintendo switch")
print(alice.furniture)

boo = [1 , 1, 2, 3]
check = []
for i in boo:
    if i not in check:
        check.append(i)
        print(i, boo.count(i))


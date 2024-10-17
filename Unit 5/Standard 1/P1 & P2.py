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
        pass
	
alice = Villager("Alice", "Koala", "guvnor")
alice.__catchphrase = "boo"
# alice.set_catchphrase("sweet dreams")
# print(alice.catchphrase)
# alice.set_catchphrase("#?!")
print(alice.__catchphrase)
# apollo = Villager("Apollo", "Eagle", "pah")
# bones = Villager("Bones", "Dog", "ruff it up")
# print(bones.greet_player("Fozhan"))
# print(apollo.name)  
# print(apollo.species)  
# print(apollo.catchphrase) 
# print(apollo.furniture) 
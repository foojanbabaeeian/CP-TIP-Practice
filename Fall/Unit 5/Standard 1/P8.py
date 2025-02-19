class Villager:
    def __init__(self, name, species, personality, catchphrase, neighbor=None):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
        self.neighbor = neighbor
    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.__catchphrase}!"
    def set_catchphrase(self, new_catchphrase):
        self.__catchphrase = new_catchphrase
    
    def add_item(self, item_name):
        self.furniture.append(item_name)
        return
    def print_inventory(self):
        if self.furniture == []:
            print("inventory empty")
        else:
            dictfurniture = {}
            for i in self.furniture:
                if i in dictfurniture:
                    dictfurniture[i] += 1
                else:
                    dictfurniture[i] = 1
            for key, val in dictfurniture.items():
                print (key, ":", val, " ", end="")
                
                
def of_personality_type(townies, personality_type):
    samepersonality = []
    for i in townies:
        if i.personality == personality_type:
            samepersonality.append(i.name)
    return samepersonality          
        
    
def message_received(start_villager, target_villager):
    pass
        
isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes, yes")
kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
isabelle.neighbor = tom_nook
tom_nook.neighbor = kk_slider
print(message_received(isabelle, kk_slider))
print(message_received(kk_slider, isabelle))
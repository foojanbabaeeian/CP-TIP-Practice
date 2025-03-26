'''Problem 1: Villager Class
A class constructor is a special method or function that is used to create and initialize a new object from a class. Define the class constructor __init__() for a new class Villager that represents characters in the game Animal Crossing. The constructor accepts three required arguments: strings name, species, and catchphrase. The constructor defines four properties for a Villager:

name, a string initialized to the argument name
species, a string initialized to the argument species
catchphrase, a string initialized to the argument catchphrase
furniture, a list initialized to an empty list'''
def problem1():
    class Villager:
        def __init__(self, name, species, catchphrase):
            self.name = name
            self.species = species
            self.catchphrase = catchphrase
            self.furniture = []

    apollo = Villager("Apollo", "Eagle", "pah")
    print(apollo.name)
    print(apollo.species) 
    print(apollo.catchphrase)
    print(apollo.furniture)

def problem2():
    class Villager:
        def __init__(self, name, species, catchphrase):
            self.name = name
            self.species = species
            self.catchphrase = catchphrase
            self.furniture = []
        def add_item(self, item_name):
            furnitures = ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"]
            if item_name in furnitures:
                self.furniture.append(item_name)
            
    alice = Villager("Alice", "Koala", "guvnor")
    print(alice.furniture)

    alice.add_item("acoustic guitar")
    print(alice.furniture)

    alice.add_item("cacao tree")
    print(alice.furniture)

    alice.add_item("nintendo switch")
    print(alice.furniture)

def problem3():
    class Villager:
        def __init__(self, name, species, personality, catchphrase):
            self.name = name
            self.species = species
            self.personality = personality
            self.catchphrase = catchphrase
            self.furniture = []
        def add_item(self, item_name):
            furnitures = ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"]
            if item_name in furnitures:
                self.furniture.append(item_name)

    def of_personality_type(townies,  personality_type):
        ans = []
        for v in townies:
            if v.personality == personality_type:
                ans.append(v.name)
        return ans

    isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
    bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
    stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")

    print(of_personality_type([isabelle, bob, stitches], "Lazy"))
    print(of_personality_type([isabelle, bob, stitches], "Cranky"))
def problem5():
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
        
    class Villager:
        def __init__(self, name, species, personality, catchphrase, neighbor=None):
            self.name = name
            self.species = species
            self.personality = personality
            self.catchphrase = catchphrase
            self.furniture = []
            self.neighbor = neighbor
        def add_item(self, item_name):
            furnitures = ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"]
            if item_name in furnitures:
                self.furniture.append(item_name)

    def of_personality_type(townies,  personality_type):
            ans = []
            for v in townies:
                if v.personality == personality_type:
                    ans.append(v.name)
            return ans
    def message_received(start_villager, target_villager):
        current_villager = start_villager
        while current_villager is not None:
            current_villager = current_villager.neighbor
            if current_villager == target_villager:
                return True        
        return False
        
    # isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
    # tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes, yes")
    # kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
    # isabelle.neighbor = tom_nook
    # tom_nook.neighbor = kk_slider

    # print(message_received(isabelle, kk_slider))
    # print(message_received(kk_slider, isabelle))
    kk_slider = Node("K.K. Slider")
    harriet = Node("Harriet")
    saharah = Node("Saharah")
    isabelle = Node("Isabelle")

    kk_slider.next = harriet
    harriet.next = saharah
    saharah.next = isabelle
    print_linked_list(kk_slider)

def problem6():
    class Node:
        def __init__(self, fish_name, next=None):
            self.fish_name = fish_name
            self.next = next

    # For testing
    def print_linked_list(head):
        current = head
        while current:
            print(current.fish_name, end=" -> " if current.next else "\n")
            current = current.next

    def catch_fish(head):
        if head is None:
            print("Aw! Better luck next time!")
            return None
        print(f"I caught a {head.fish_name}!")
        head = head.next
        return head
    fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
    empty_list = None

    print_linked_list(fish_list)
    print_linked_list(catch_fish(fish_list))
    print(catch_fish(empty_list))

class Node:
    def __init__(self, fish_name, next=None):
        self.fish_name = fish_name
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.fish_name, end=" -> " if current.next else "\n")
        current = current.next
def restock(head, new_fish):
    current = head 
    while current:
        if current.next == None:
            current.next = Node(new_fish)
            break
        current = current.next
    return head
    
def fish_chances(head, fish_name):
    dict = {}
    current = head
    while current:
        if current.fish_name in dict:
            dict[current.fish_name] += 1
        else:
            dict[current.fish_name] = 1
        current = current.next
    if fish_name in dict:
        return round(dict[fish_name] / sum(dict.values()), 2)
    return 0.00

# fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
# print(fish_chances(fish_list, "Dace"))
# print(fish_chances(fish_list, "Rainbow Trout"))
# fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
# print_linked_list(restock(fish_list, "Rainbow Trout"))
    


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

def find_max(head):
    maximum = head.value
    current = head
    while current:
        if current.value > maximum:
            maximum = current.value
        current = current.next
    return maximum
def remove_tail(head):
    if head is None:
        return None
    if head.next is None:
        return None 
        
    current = head
    while current.next: 
        current = current.next

    current= None 
    return head

head1 = Node(5, Node(6, Node(7, Node(8))))

# # Linked List: 5 -> 6 -> 7 -> 8
# print(find_max(head1))

# head2 = Node(5, Node(8, Node(6, Node(7))))

# # Linked List: 5 -> 8 -> 6 -> 7
# print(find_max(head2))
head = Node("Isabelle", Node("Alfonso", Node("Cyd")))

# Linked List: Isabelle -> Alfonso -> Cyd
print_linked_list(remove_tail(head))

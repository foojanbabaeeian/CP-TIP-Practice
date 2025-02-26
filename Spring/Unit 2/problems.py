'''
Problem 1: Counting Treasure
Captain Blackbeard has a treasure map with several clues that point to different locations on an island. Each clue is associated with a specific location and the number of treasures buried there. Given a dictionary treasure_map where keys are location names and values are integers representing the number of treasures buried at those locations, write a function total_treasures() that returns the total number of treasures buried on the island.

def total_treasure(treasure_map):
    pass
Example Usage:

treasure_map1 = {
    "Cove": 3,
    "Beach": 7,
    "Forest": 5
}

treasure_map2 = {
    "Shipwreck": 10,
    "Cave": 20,
    "Lagoon": 15,
    "Island Peak": 5
}

print(total_treasures(treasure_map1)) 
print(total_treasures(treasure_map2)) 
Example Output:

15
50
'''
def problem1():

    def total_treasures(treasure_map):
        return sum(treasure_map.values())

    treasure_map1 = {
        "Cove": 3,
        "Beach": 7,
        "Forest": 5
    }

    treasure_map2 = {
        "Shipwreck": 10,
        "Cave": 20,
        "Lagoon": 15,
        "Island Peak": 5
    }

    print(total_treasures(treasure_map1)) 
    print(total_treasures(treasure_map2)) 


'''
Problem 2: Pirate Message Check
Taken captive, Captain Anne Bonny has been smuggled a secret message from her crew. She will know she can trust the message if it contains all of the letters in the alphabet. Given a string message containing only lowercase English letters and whitespace, write a function can_trust_message() that returns True if the message contains every letter of the English alphabet at least once, and False otherwise.

def can_trust_message(message):
    pass
Example Usage:

message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"

print(can_trust_message(message1))
print(can_trust_message(message2))
Example Output:

True
False
'''
def problem2():
    def can_trust_message(message):
        message = message.replace(" ", "")
        return True if len(set(message)) == 26 else False

    message1 = "sphinx of black quartz judge my vow"
    message2 = "trust me"

    print(can_trust_message(message1))
    print(can_trust_message(message2))  


'''
Problem 3: Find All Duplicate Treasure Chests in an Array
Captain Blackbeard has an integer array chests of length n where all the integers in chests are in the range [1, n] and each integer appears once or twice. Return an array of all the integers that appear twice, representing the treasure chests that have duplicates.

def find_duplicate_chests(chests):
    pass
Example Usage:

chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
chests2 = [1, 1, 2]
chests3 = [1]

print(find_duplicate_chests(chests1))
print(find_duplicate_chests(chests2))
print(find_duplicate_chests(chests3))
Example Output:

[2, 3]
[1]
[]
'''
def problem3():
    def find_duplicate_chests(chests):
        dict = {}
        for boo in chests:
            if boo in dict:
                dict[boo] += 1
            else:
                dict[boo] = 1
        result = []
        for sth in dict:
            if dict[sth] >= 2:
                result.append(sth)
        return result
        

    chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
    chests2 = [1, 1, 2]
    chests3 = [1]

    print(find_duplicate_chests(chests1))
    print(find_duplicate_chests(chests2))
    print(find_duplicate_chests(chests3))

'''
Problem 4: Booby Trap
Captain Feathersword has found another pirate's buried treasure, but they suspect it's booby-trapped. The treasure chest has a secret code written in pirate language, and Captain Feathersword believes the trap can be disarmed if the code can be balanced. A balanced code is one where the frequency of every letter present in the code is equal. To disable the trap, Captain Feathersword must remove exactly one letter from the message. Help Captain Feathersword determine if it's possible to remove one letter to balance the pirate code.

Given a 0-indexed string code consisting of only lowercase English letters, write a function is_balanced() that returns True if it's possible to remove one letter so that the frequency of all remaining letters is equal, and False otherwise.

def is_balanced(code):
    pass
Example Usage:

code1 = "arghh"
code2 = "haha"

print(is_balanced(code1)) 
print(is_balanced(code2)) 
Example Output:

True
Explanation: Select index 4 and delete it: word becomes "argh" and each character has a frequency of 1.

False
Explanation: They must delete a character, so either the frequency of "h" is 1 and the f
'''
def problem4():
    def is_balanced(code):
        dict = {}
        for boo in code:
            if boo in dict:
                dict[boo] += 1
            else:
                dict[boo] = 1
        # same numbers and then 1 that is different only by 1
        # 1 2 checking if there exists two values that have a diff of 1 and then check that the rest of the values are equal to the smaller value 
        # temo var that holds the first one and we iterate through the values and we can keep the c  
        #                                                                         if the differnce is 1:  
        #                                                                         elif it is more than 1:
        val = list(dict.values())
        val.sort()
        diff = 0 
        flag = False
        for i in range(len(val)):
            if i == 0:
                first = val[i]
                continue
            diff = abs(val[i] - first)
            if diff > 1:
                return False
            elif diff == 1:
                if flag == True:
                    return False
                flag = True 
        print(val, diff)

        return flag 
    code1 = "arghh"
    code2 = "haha"

    print(is_balanced(code1)) 
    print(is_balanced(code2)) 

'''
Problem 5: Overflowing With Gold
Captain Feathersword and their crew has discovered a list of gold amounts at various hidden locations on an island. Each number on the map corresponds to the amount of gold at a specific location. Captain Feathersword already has plenty of loot, and their ship is nearly full. They want to find two distinct locations on the map such that the sum of the gold amounts at these two locations is exactly equal to the amount of space left on their ship.

Given an array of integers gold_amounts representing the amount of gold at each location and an integer target, return the indices of the two locations whose gold amounts add up to the target.

Assume that each input has exactly one solution, and you may not use the same location twice. You can return the answer in any order.

def find_treasure_indices(gold_amounts, target):
    pass
Example Usage:

gold_amounts1 = [2, 7, 11, 15]
target1 = 9

gold_amounts2 = [3, 2, 4]
target2 = 6

gold_amounts3 = [3, 3]
target3 = 6

print(find_treasure_indices(gold_amounts1, target1))  
print(find_treasure_indices(gold_amounts2, target2))  
print(find_treasure_indices(gold_amounts3, target3))  
Example Output:

[0, 1]
[1, 2]
[0, 1]'''

def find_treasure_indices(gold_amounts, target):
    # index , key
    dict = {}
    for i in range(len(gold_amounts)):
        dict[gold_amounts[i]] = i
    print(dict)
    for i in range(len(gold_amounts)):
        if target - dict[gold_amounts[i]] in dict and dict[target - dict[gold_amounts[i]]] != i:
            print(dict, i, dict[target - dict[gold_amounts[i]]])
            return [dict[target - dict[gold_amounts[i]]], i] 
        
gold_amounts1 = [2, 7, 11, 15]
target1 = 9

gold_amounts2 = [3, 2, 4]
target2 = 6

gold_amounts3 = [3, 3]
target3 = 6

print(find_treasure_indices(gold_amounts1, target1))  
print(find_treasure_indices(gold_amounts2, target2))  
print(find_treasure_indices(gold_amounts3, target3))  
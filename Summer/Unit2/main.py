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
    def total_treasure(treasure_map):
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

    print(total_treasure(treasure_map1)) 
    print(total_treasure(treasure_map2)) 



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
        message = message.replace(' ', '')
        print(set(message), len(set(message)))
        if len(set(message)) == 26:
            

            return True
        else:
            return False
        
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
        duplicates = {}
        dup_list = []
        for item in chests:
            if item in duplicates:
                dup_list.append(item)
            else:
                duplicates[item] = 1
        return dup_list
        

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
Explanation: They must delete a character, so either the frequency of "h" is 1 and the frequency of "a" is 2, or vice vers
'''

def is_balanced(code):
    check_dict = {}
    for char in code:
        if char in check_dict:
            check_dict[char] +=1
        else:
            check_dict[char] = 1
    if len(check_dict) == 1:
        return True
    list_of_the_frequencies = check_dict.values()
    frequencies = {}
    for char in list_of_the_frequencies:
        if char in frequencies:
            frequencies[char] +=1
        else:
            frequencies[char] = 1
    '''
    {1:3, 2:1}
    {2:2}
    '''
    if len(frequencies.keys()) >2:
        return False
    # elif len(frequencies.keys()) == 1:
    #     return True
    elif 1 in frequencies.keys() and frequencies[1] == 1:
        return True
    elif len(frequencies.keys()) == 2 and min(frequencies.values()) == 1 and max(frequencies.keys()) - min(frequencies.keys()) == 1:
        return True
    else:
        return False



'''

1.  3 or more frequencies --> False
2.  1 frequency --> True 
3.  if 1 is in the frequency table happening only once and then rest are all the same --> True
4.  There are 2 frequencies and one of the frequncies is one less  4, 4, 4, 5


2,2, 2, 3 ===
2, 2, 2, 3

4, 4, 1
1, 4, 4

aaa bbbb ccccc

aaaaaaa

# we have one extra element that is appearing only once and everything else is the same
we have one that is one higher than the rest 
'''
code1 = "arghh"
code2 = "aaaaaa"
code3 = "haha"
code4 = "abbbbb"

'''
{1:3, 2:1}
{2:2}
'''
print(is_balanced(code3)) 
print(is_balanced(code4)) 
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

# print(find_treasure_indices(gold_amounts1, target1))  
# print(find_treasure_indices(gold_amounts2, target2))  
# print(find_treasure_indices(gold_amounts3, target3))  


'''
Problem 1: Balanced Art Collection
As the curator of an art gallery, you are organizing a new exhibition. You must ensure the collection of art pieces are balanced to attract the right range of buyers. A balanced collection is one where the difference between the maximum and minimum value of the art pieces is exactly 1.

Given an integer array art_pieces representing the value of each art piece, write a function find_balanced_subsequence() that returns the length of the longest balanced subsequence.

A subsequence is a sequence derived from the array by deleting some or no elements without changing the order of the remaining elements.

def find_balanced_subsequence(art_pieces):
    pass
Example Usage:

art_pieces1 = [1,3,2,2,5,2,3,7]
art_pieces2 = [1,2,3,4]
art_pieces3 = [1,1,1,1]

print(find_balanced_subsequence(art_pieces1))
print(find_balanced_subsequence(art_pieces2))
print(find_balanced_subsequence(art_pieces3))
Example Output:

5
Example 1 Explanation:  The longest balanced subsequence is [3,2,2,2,3].

2
0

'''

# def find_balanced_subsequence(art_pieces):

'''
Problem 2: Verifying Authenticity
Your art gallery has just been shipped a new collection of numbered art pieces, and you need to verify their authenticity. The collection is considered "authentic" if it is a permutation of an array base[n].

The base[n] array is defined as [1, 2, ..., n - 1, n, n], meaning it is an array of length n + 1 containing the integers from 1 to n - 1 exactly once, and the integer n twice. For example, base[1] is [1, 1] and base[3] is [1, 2, 3, 3].

Write a function is_authentic_collection that accepts an array of integers art_pieces and returns True if the given array is an authentic array, and otherwise returns False.

Note: A permutation of integers represents an arrangement of these numbers. For example [3, 2, 1] and [2, 1, 3] are both permutations of the series of numbers 1, 2, and 3.

def is_authentic_collection(art_pieces):
    pass
Example Usage:

collection1 = [2, 1, 3]
collection2 = [1, 3, 3, 2]
collection3 = [1, 1]

print(is_authentic_collection(collection1))
print(is_authentic_collection(collection2))
print(is_authentic_collection(collection3))
'''
def is_authentic_collection(collection):
    dict = {}
    for boo in collection:
        if boo in dict:
            dict[boo] += 1
        else:
            dict[boo] = 1
    for i in range(1, len(collection)):
        if i not in dict:
            return False
        if dict[i] != 1:
            return False
    if dict[len(collection)] != 2:
        return False
    return True




collection1 = [2, 1, 3]
collection2 = [1, 3, 3, 2]
collection3 = [1, 1]

print(is_authentic_collection(collection1))
print(is_authentic_collection(collection2))
print(is_authentic_collection(collection3))

'''
Problem 4: Gallery Subdomain Traffic
Your gallery has been trying to increase it's online presence by hosting several virtual galleries. Each virtual gallery's web traffic is tracked through domain names, where each domain may have subdomains.

A domain like "modern.artmuseum.com" consists of various subdomains. At the top level, we have "com", at the next level, we have "artmuseum.com", and at the lowest level, "modern.artmuseum.com". When visitors access a domain like "modern.artmuseum.com", they also implicitly visit the parent domains "artmuseum.com" and "com".

A count-paired domain is represented as "rep d1.d2.d3" where rep is the number of visits to the domain and d1.d2.d3 is the domain itself.

For example, "9001 modern.artmuseum.com" indicates that "modern.artmuseum.com" was visited 9001 times.
Given an array of count-paired domains cpdomains, return an array of the count-paired domains of each subdomain. The order of the output does not matter.

def subdomain_visits(cpdomains):
    pass
Example Usage:

cpdomains1 = ["9001 modern.artmuseum.com"]
cpdomains2 = ["900 abstract.gallery.com", "50 impressionism.com", 
              "1 contemporary.gallery.com", "5 medieval.org"]

print(subdomain_visits(cpdomains1))
print(subdomain_visits(cpdomains2))
Example Output:

["9001 artmuseum.com", "9001 modern.artmuseum.com", "9001 com"]

["901 gallery.com", "50 impressionism.com", "900 abstract.gallery.com", "5 medieval.org", "5 org",
"1 contemporary.gallery.com", "951 com"]
'''

def subdomain_visits(cpdomains):
    for element in cpdomains:
        subdomains = element.split(" ")
        print(subdomains)
        # [9001, "modern.artmuseum.com"]
        subdomains[1] = subdomains[1].split(".")
        print(subdomains)
        print(set(subdomains[1]))
        # ["modern", "artmuseum", "com"]
        dict = {}


cpdomains1 = ["9001 modern.artmuseum.com"]
cpdomains2 = ["900 abstract.gallery.com", "50 impressionism.com", 
              "1 contemporary.gallery.com", "5 medieval.org"]

print(subdomain_visits(cpdomains1))
print(subdomain_visits(cpdomains2))
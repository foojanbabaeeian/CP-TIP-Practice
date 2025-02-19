# problem 1
def welcome():
	print("Welcome to The Hundred Acre Wood!")

# problem 2
def greeting(name):
	print(f"Welcome to The Hundred Acre Wood {name}! My name is Fozhan Babaeiyan.")

# problem 3
def print_catchphrase(character):
	if character == "Pooh":
		print("Oh bother!")
	elif character == "Tigger":
		print("TTFN: Ta-Ta for now!")
	elif character == "Eeyore":
		print("Thanks for noticing me.")
	elif character == "Christopher Robin":
		print("Silly old bear.")
	else:
		print(f"Sorry! I don't know {character} catchphrase!"
)
a = 1
b = 2
		
# print("{b} + {a} = {c}".format(b = b, a = a, c= a+b))

# problem 4
def get_item(items, x):
	if x >= len(items):
		return None
	return items[x]

# items = ["piglet", "pooh", "roo", "rabbit"]
# x = 2
# print(get_item(items, x))

# items = ["piglet", "pooh", "roo", "rabbit"]
# x = 5
# print(get_item(items, x))

# problem 5
def sum_honey(hunny_jars):
	sum = 0
	for jar in hunny_jars:
		sum += jar
	return sum
	# return sum(hunny_jars)

# problem 6

def doubled(hunny_jars):
    for i in range(len(hunny_jars)):
        hunny_jars[i] *= 2
    return hunny_jars


hunny_jars = [1, 2, 3]
print(doubled(hunny_jars))

# Advanced problems we worked on 

def tiggerfdhdddy(s):
    #not memory efficient 
	tiger = "tiger"
	byetiger = ""
	for letter in s:
            if letter not in tiger:
                byetiger += letter


def tiggerfy(s):
    tiger = "tiger"
    s = list(s)
    for letter in s:
        if letter not in tiger:
            byetiger += letter
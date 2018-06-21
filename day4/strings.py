"""
Strings - these are collections of characters. They are represented by
either single or double quotes.
"""

name = "Victor"
abc = "abcdefghijklmnopqrstuvwxyz"

# Strings have length
print(len(abc)) # prints 26
print(len(name)) # prints 6

# elements in a string can be accessed like elements in a list
print(name[0]) # Print V
print(name[0:3]) # Prints Vic
print(name.index("r")) # Prints 5

# Strings are immutable however, meaning they cannot change
# so something like this won't work
# name[1] = "e"

# We can check for membership of a string very easily
print('a' in name) # False
print('Vic' in name) # True

# We cannot do this for lists
print(['a', 'b'] in ['a', 'b', 'c', 'd']) # False

# We can convert strings into lists

abc_list = list(abc)


# Strings have a special method (function) called join
# This joins other string elements into a new string
l = ['a', 'b', 'r', 'a', 'c', 'a', 'd', 'a', 'b', 'r', 'a']

s = "".join(l)
print(s) # prints abracadabra

phrase = "The quick brown fox jumped over the lazy dog"

words = phrase.split(" ")
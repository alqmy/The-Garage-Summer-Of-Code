"""
Lists are a datatype you can use to store a collection of different pieces
of information as a sequence under a single variable name. 

(Datatypes you've already learned about include strings, numbers, and booleans.)
"""

zoo_animals = ["pangolin", "cassowary", "sloth", ]
# One animal is missing!

if len(zoo_animals) > 3:
    print( "The first animal at the zoo is the " + zoo_animals[0])
    print( "The second animal at the zoo is the " + zoo_animals[1])
    print( "The third animal at the zoo is the " + zoo_animals[2])
    print( "The fourth animal at the zoo is the " + zoo_animals[3])


"""
You can get the length of lists using the len function
"""

print(len(zoo_animals))

# Exercise
suitcase = [] 
suitcase.append("sunglasses")

# Your code here!

list_length = ________ # Set this to the length of suitcase

print "There are %d items in the suitcase." % (list_length)
print suitcase


"""
Sometimes, you only want to access a portion of a list.
"""
suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

# The first and second items (index zero and one)
first = suitcase[0:2]

# Third and fourth items (index two and three)
middle = 

# The last two items (index four and five)
last =  

"""
We can iterate (go through) a list using the for loop
"""

my_list = [1,9,3,8,5,7]

for number in my_list:
    print(number)

"""
Lists have basic functions built in
"""

numbers = [1,9,3,8,5,7]
print(numbers)

# this adds 100 to the end of the list
numbers.append(100)
print(numbers)

# this adds 75 to the third position of the list
# and moves the rest of the numbers to the right by 1 
numbers.insert(2, 75)
print(numbers)


# this will remove the item at index from the list 
# and return it to you
number = numbers.pop(1) # removes item at position 1
print(numbers)
print(number)

# Removes 1 from the list,
# NOT the item at index 1
numbers.remove(1)
print(numbers)

# del is like .pop in that it will remove
# the item at the given index, but it won't return it:
del(numbers[1])
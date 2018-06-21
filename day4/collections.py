"""
Python as a wide array of collection datatypes. These are
variables that can hold many values under a single name.
"""

# Lists - this is the most common type of collection
animals = ["Dog", "Cat", "Horse"]
print(animals[1])  # prints Cat

# Lists are mutable, meaning they can be changed
animals[2] = "Big Horse"  # This changes the value at position 2
animals.append("Zorse")  # This adds a Zorse to the end of the list

# Lists have length
l = len(animals)
print(l)  # prints 4


# Tuples - tuples are like lists, but they are immutable.
# meaning they cannot change once they are defined.
# They are constant
color_red = (255, 0, 0)  # Color red in RGB mode
coordinate = (1.5, 2.5)  # Coordinate on a plane
WEEKDAYS = ("Monday", "Tuesday",
            "Wednesday", "Thursday", "Friday",
            "Saturday", "Sunday")

# We can access a single element much like Lists
print(WEEKDAYS[0])  # Prints Monday

# We can get the length of a tuple much like Lists
print(len(WEEKDAYS))  # prints 7

# We can count instances of elements
WEEKDAYS.count('Monday')  # 1

# We CANNOT however change the elements of a tuple once they are
# defined. They stay that way forever
# WEEKDAYS[0] = "Conday" is not allowed


# Sets - A set is a collection of unique elements
# They are like lists, but if you insert an element
# twice the duplicates are eliminated

animal_set = {'cat', 'dog', 'goldfish', 'cat'}  # cat will only appear once
print(animal_set)

# We can perform various operations on sets
even_numbers = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
natural_numbers = {-1, -2, -3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# subtraction: natural numbers which are not even
print(natural_numbers - even_numbers)

# union: numbers which are natural or even
print(natural_numbers | even_numbers)

# intersection: numbers which are natural and even
print(natural_numbers & even_numbers)

# numbers which are natural or even but not both
print(natural_numbers ^ even_numbers)


# Ranges - another immutable collection type, used to create
# ranges of integers

# prints the integers from 0 to 9
print(list(range(10)))

# print the integers from 1 to 10
print(list(range(1, 11)))

# print the odd integers from 1 to 10
print(list(range(1, 11, 2)))


# Dictionaries - We can use it to store key-value pairs.

marbles = {'red': 34, 'green': 30, 'brown': 31}

personal_details = {
    "name": "Jane Doe",
    "age": 38,
}

print(marbles["green"])
print(personal_details["name"])

# modify a value
marbles["red"] += 3
personal_details["name"] = "Jane Q. Doe"


# Conversion between collection types

car_brands = ["Kia", "Ford", "Chevy", "Toyota", "BMW", "Toyota"]

# creates a set from the car_brands and removes duplicates
car_brand_set = set(car_brands)

# creates a list from a set
car_brands_unique = list(car_brand_set)

# creates a tuple from a set
car_brand_tuple = tuple(car_brand_set)
print(car_brand_tuple)

# creates a tuple from a list
car_brand_tuple = tuple(car_brands)
print(car_brand_tuple)

colors = list(marbles)  # the keys are used by default
counts = list(marbles.values())  # but we can use a view to get the values
marbles_Set = set(marbles.items())  # or the key-value pairs


# Python doesn't know how to convert this into a dictionary
# dict([1,2,3,4])

# but this will work
dict([(1, 2), (3, 4)])  # {1: 2, 3: 4}
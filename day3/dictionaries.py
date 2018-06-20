"""
Dictionaries are like lists, but you access values using a key
instead of an index.  A key can be any string or number. 
"""


"""
Dictionaries are enclosed in curly braces, like so
"""

d = {'key1' : 1, 'key2' : 2, 'key3' : 3}

residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}
print(residents['Puffin'])

"""
You can add values by adding a key and setting the value
"""

residents['Panther'] = 200

# you can use the same syntax to change values
residents['Panther'] = 100
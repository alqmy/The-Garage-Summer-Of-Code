"""
Modules are libraries of python code that have been collected
together that give specific functionality
"""

# imports that python math libaries
import math

number = 5

# sqrt is a function in the math libarie
number_squared = math.sqrt(number)
print(number_squared)

"""
we can import only what we need using the from syntax
"""

# this imports only the factorial function 
# and the pi constant from the math library
from math import factorial, pi

fact = factorial(5)
print(pi)

"""
We can also import everything from a module
"""

# import everything from the calendar module
from datetime import *

# xmas = datetime.date(2018, 12, 25)
xmas = date(2018, 12, 25)
print(xmas)

# change name of import
import base64 as b64

"""
Variables can only reach the area in which they are defined, 
which is called scope. Think of it as the area of code where 
variables can be used. Python supports global variables 
(usable in the entire program) and local variables.

By default, all variables declared in a function are local 
variables. To access a global variable inside a function, it’s 
required to explicitly define ‘global variable’. 
"""

# Examples
z = 3

def f(x,y):
    print('You called f(x,y) with the value x = ' + str(x) + ' and y = ' + str(y))
    print('x * y = ' + str(x*y))
    z = 4 # cannot reach z, so THIS WON'T WORK
    
f(3,2)
print(z)    # This will print 3 instead of 4, because
            # this z is defined in global scope
            # and is outside of the scope of f

# In order for the function to affect variables outside of its scope
# those variables must be marked as global.
def global_f(x, y):
    global z
    print('You called f(x,y) with the value x = ' + str(x) + ' and y = ' + str(y))
    print('x * y = ' + str(x*y))
    # This will work, because z is explicitly global
    # for this function
    z = 4

global_f(3,2)
print(z)    # z is now 4


"""
Functions are an exception to the rule of global scope.
All functions can reach other functions defined in the
scope outside of them.
"""
def af():
    "function that does nothing"
    pass

def bf():
    "function that does nothing but call a"
    af() # b can reach a, no need to mark as global

"""
Here are some examples of different variable scopes in Python
"""

# This is a global variable
a = 0

if a == 0:
    # This is still a global variable
    b = 1

def my_function(c):
    # this is a local variable
    d = 3
    print(c)
    print(d)

# Now we call the function, passing the value 7 as the first and only parameter
my_function(7)

# a and b still exist
print(a)
print(b)

# c and d don't exist anymore -- these statements will give us name errors!
# print(c)
# print(d)
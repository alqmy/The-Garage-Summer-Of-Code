# What Good are Functions?
# You might have considered the situation where you would 
# like to reuse a piece of code, just with a few different 
# values. Instead of rewriting the whole code, it's much cleaner 
# to define a function, which can then be used repeatedly.

def tax(bill):
    """Adds 8% tax to a restaurant bill."""
    bill *= 1.08
    print("With tax: %f" % bill)
    return bill

def tip(bill):
    """Adds 15% tip to a restaurant bill."""
    bill *= 1.15
    print("With tip: %f" % bill)
    return bill

meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)


# Functions can call other functions
def fun_one(n):
    return n * 5

def fun_two(m):
    return fun_one(m) + 7

print(fun_two(500)) # 25007
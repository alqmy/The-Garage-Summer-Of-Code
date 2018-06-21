"""
Shipping module contains the stuff needed to handle shipping
"""

def cost(weight):
    "Calculates the cost based on weight in lbs"
    if weight >= 100:
        return weight * 5 + 10
    elif weight >= 1 and weight <= 5:
        return weight * 2 - 1
    else:
        return weight * 5


def can_ship(weight, distance):
    """
    Determines if we can ship a package based on its weight,
    and distance traveled.
    """

    if weight * distance < 1000:
        return True
    else:
        return False

def menu():
    print("""
    ======== WELCOME TO THE PYTHON POSTAL SERVICE ===
    1. Calculate Cost
    2. Determine if shippable
    0. Exit 
    """)
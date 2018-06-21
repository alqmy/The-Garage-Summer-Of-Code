"""
PPS  - Python Postal Service
Example of making your own modules
"""
import shipping
from os import system

# tell the os to clear the screen
def clear_screen():
    system("clear")

# wait for the user to press enter
def wait():
    input("Press enter to continue")


if __name__ == "__main__":
    shipping.menu()
    option = int(input("Enter option: "))

    while option != 0:
        if option == 1:
            clear_screen()
            print("Calculating cost")
            weight = int(input("Enter weight: "))
            cost = shipping.cost(weight)

            print("Your shipping cost is $%d" % cost)
            wait()
        elif option == 2:
            clear_screen()
            print("Determening if we can ship")
            weight =  int(input("Enter weight: "))
            distance = int(input("Enter distance in miles: "))

            can_ship = shipping.can_ship(weight, distance)
            if can_ship:
                print("We can ship that")
            else:
                print("Sorry, we can't ship that")
            wait()

        clear_screen()
        shipping.menu()
        option = int(input("Enter option: "))
    
    clear_screen()
    print("Goodbye!")

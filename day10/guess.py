import random

n = random.randint(1, 100)

tries = 0
max_tries = 20

while tries < max_tries:
    guess = int(input())

    difference = abs(guess - n)

    if guess != n:
        if difference > 10:
            print("Colder")
        elif difference < 10 or difference > 5:
            print("Warmer")
        elif difference < 5 or difference > 1:
            print("Hot")
    else:
        print("You got it!")
        break
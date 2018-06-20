import random

villans = [
    {
        'name': 'Batman',
        'health': 100,
        'bite_damage': -5,
        'claw_damage': -1,
        'punch': -10,
        'escape_chance': 10,  # 10% of escaping
    },
    {
        'name': 'Spock',
        'health': 100,
        'bite_damage': -25,
        'claw_damage': -5,
        'punch': -2,
        'escape_chance': 50,  # 10% of escaping
    },
    {
        'name': 'Gork',
        'health': 100,
        'bite_damage': -10,
        'claw_damage': -2,
        'punch': -5,
        'escape_chance': 75,  # 10% of escaping
    }
]


def generate(num):
    index = random.randint(0, 2)
    if num % (index + 1) == index:
        return villans[index]
    else:
        return None


level = [generate(x) for x in range(1, 11)]


print("""
You enter a dark hallway.
You can move forward or exit.
What do you do?
""")

player_health = 100
player_pos = 0
valid_moves = ["forward"]
player_dead = False

move = str(input())

while move != "exit" or not player_dead:
    print("Health " + str(player_health))
    if move not in valid_moves:
        print("You can't do that yet")
    else:
        if move == "forward" and player_pos < len(level):
            player_pos += 1
            print("You move forward one square")

            valid_moves.append("backward")

            if player_pos == len(level) - 1:
                valid_moves.remove("forward")

        elif move == "backward" and player_pos > 0:
            player_pos -= 1
            print("You move back one square")

            if player_pos == 0:
                valid_moves.remove("backward")

        print("You are at position {}".format(player_pos))

        # check if there is a viallan here
        if level[player_pos] != None:
            # deal with the viallan
            valid_moves += ['bite', 'claw']
            valid_moves.remove('forward')
            escape = False
            villan = level[player_pos]

            print("You are now fighting")
            print(villan['name'])
            name = villan['name']

            # mientras no escapas y el villano no esta debilitado
            # tienes que pelear
            while not escape or villan['health'] != 0:
                print("Health " + str(player_health))
                print(name + " Health " + str(villan['health']))
                print("What do you do?")
                move = str(input())
                if move == "back":
                    "calculate chance of escpaing"
                elif move == "bite":
                    "bite"
                    damage = villan['bite_damage']
                    villan['health'] += damage
                elif move == "claw":
                    "claw"
                    damage = villan['claw_damage']
                    villan['health'] += damage
                
                print("You {} at {}".format(move, name))

                if villan['health'] != 0 or not escape:
                    player_damage = villan['punch']

                    print("{} hits you and you loose {} health".format(
                        name, player_damage))

                    player_health += player_damage

                    if player_health == 0:
                        player_dead = True
                
    move = str(input())

if player_dead:
    print("You died")

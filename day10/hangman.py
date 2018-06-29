from random import randint

words = """charge
desk
vision
restoration
coast
electronics
grounds
swim
attraction
barrel
deadly
stroke
surprise
base
fitness
galaxy
ditch
slant
headline
mosque
referral
social
army
forget
creation
crew
motivation
way
ask
prescription
pray
wander
veil
request
frozen
sharp
flat
fare
dorm
blue jean
cylinder
video
performance
tin
union
pneumonia
trust
pollution
association
opinion
feedback
seek
sunshine
rally
autonomy
guilt
surgeon
clear
healthy
detail
reception
run
right wing
defeat
species
labour
bullet
pleasure
crowd
elephant
tax
hip
advocate
attractive
shave
credit card
qualify
cheat
crosswalk
ex
owe
company
node
government
world
painter
intelligence
threaten
snap
minister
production
ideology
double
beautiful
elaborate
defendant
entitlement
order
inappropriate
sport""".split("\n")

chosen_word = words[randint(0, len(words) - 1)]
running_guess = ["_" for l in chosen_word]

while True:
    running = "".join(running_guess)
    print("Word is %d letters long" % len(chosen_word))
    print("Running guess: %s" % running)
    guess = running

    if guess == chosen_word:
        print("You got it")
        break
    guess = input("Enter a word or character: ")

    if len(guess) > 1:
        if guess != chosen_word:
            print("Wrong guess")
    elif guess in chosen_word:
        n = chosen_word.count(guess)
        print("The letter appears %d times in the word" % n)
        
        for start, _ in enumerate(chosen_word):
            i = chosen_word.find(guess, start)
            if i != -1:
                running_guess[i] = guess
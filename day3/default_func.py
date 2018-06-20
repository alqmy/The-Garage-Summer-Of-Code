def greet(who="Stranger"):
    print("Hello, " + who)

def complicated_greet(who):
    if who == None:
        who = "Stranger"
    print("Hello, " + who)

greet("World")
greet()

def out_of_order(first=8, middle=7, last=20):
    print(first)
    print(middle)
    print(last)

out_of_order(0, 1, 35)
out_of_order()
out_of_order(0)
out_of_order(0, last=25)

def out_of_order2(first, middle=7, last=20):
    print(first)
    print(middle)
    print(last)

out_of_order2(10)

# not valid
# def out_of_order3(first=1, middle, last=20):
#     print(first)
#     print(middle)
#     print(last)
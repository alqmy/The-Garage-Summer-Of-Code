my_list = list(range(10))

print(my_list[0])

i = 0

while i < len(my_list):
    print(my_list[i])

    i += 1

for i in my_list:
    print(i)


if 5 in my_list:
    print("Five is in the list")=

def my_func(x, y, z):
    return x * y * z

def power(x, y):
    result = 1
    while y > 0:
        result *= x
        y -= 1
    
    return result


res = "Hello, " + "World"

def sum(x, y = 10):
    return x + y

def greeting(who="World"):
    return "Hello, " + who

print(greeting())
print(greeting("Victor"))

my_greeting = greeting("Mundo")
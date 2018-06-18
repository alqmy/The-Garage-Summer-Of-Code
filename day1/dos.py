r = 5

a = int(input())

if a % 2 == 0 or (r % 2 == 0 and a == 5):
    print("both are divisible")
elif a % 2 == 0:
    print("only a is divisible")
else:
    print("none are divisible")


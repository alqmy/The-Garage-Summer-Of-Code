with open("example.txt", mode="r+b") as binary:
    first_10 = binary.read(10)
    
    one = binary.read(1)
    b = bin(one[0])
    print(b)

    print(first_10)
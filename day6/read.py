
example = open("example.txt", mode='r')

first_10_bytes = example.read(10)

print(example)
print(first_10_bytes)

example.seek(0)

lines = example.readlines()

for line in lines:
    print(line, end='')

print('\n')
example.seek(0)
for line in example:
    print(line, end='')

print('\n')
example.seek(5)
val = example.read(1)
print(val)

example.close()


with open("example.txt") as example2:
    for line in example2:
        print(line, end='')
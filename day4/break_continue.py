"""
Sometimes we may want to skip portions or all of a loop. We
do this with break and continue
"""

# break - you can use this to exit out of a loop immediately
x = 1

# This will only print 1, 2, 3, 4
while x <= 10:
    # break out of the loop if we reach 5 before reaching 10
    if x == 5:
        break

    print(x)
    x += 1

# continue - we can use this to skip an iteration of a loop

# This will print 1, 2, 3, 4, 6, 7, 8, 9, and 10, but not print 5
for x in range(1, 10 + 1):
    # skip the rest of the loop if we hit 5
    if x == 5:
        continue
    
    print(x)

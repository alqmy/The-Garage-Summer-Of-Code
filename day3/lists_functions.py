"""
You can have lists as arguments in functions
"""


def maximum(numbers):
    "Calculates the maximum number in a list"
    max_number = numbers[0]

    for current in numbers:
        if max_number < current:
            max_number = current

    return max_number


my_list = [1, 20, 25, 80, 11, 122, 1]
the_max = maximum(my_list)

print(the_max)

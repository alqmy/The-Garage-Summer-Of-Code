"""
You can have lists as arguments in functions
"""


def maximum(numbers):
    "Calculates the maximum number in a list"
    max_number = numbers[0]

    for number in numbers:
        if max_number < number:
            max_number = number

    return max_number


the_max = maximum([1, 20, 25, 80, 11, 122, 1])

print(the_max)

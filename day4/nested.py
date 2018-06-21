"""
In some cases you want to make decisions depending on other decisions.
In Python you usually do this with nested if statements.
"""

# Example
def ship(weight):
    "determines cost based on weight"
    if weight <= 1000:
        if weight <= 300:
            cost = 5
        # this else belongs to the second if
        else:
            cost = 5 + 2 * round((weight - 300)/100)

        print("Your parcel will cost R%d." % cost)

    # this else belongs to the first if
    else:
        print("Maximum weight for small parcel exceeded.")
        print("Use large parcel service instead.")
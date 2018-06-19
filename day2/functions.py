def my_name():
    print("name")

# calls my_name
my_name()

def square(x):
    # devuelve el valor
    return x * x

n = square(5)
print(n)

# declarandro función power
# que recibe dos paramatros y los
# llamo "x" y "n".
def power(x, n):
    p = 1
    for i in range(n):
        # p = p * x
        p *= x
    return p


power_2 = power(2, 2) # 4
print(power_2)



# define una función que devuelva una nota ("A", "B", ...)
# para el numero que le pase

def many_return(x):
    if x % 2 == 0:
        return "even"
    else:
        return "odd"

print(many_return(5))

# def nota(puntos, valor_de_examen):
#     porcentage = puntos / valor_de_examen
#     grade(porcentage)

# example of one function calling another function
def even_or_odd(n):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"

def can_fly(wing_span):
    oddness = even_or_odd(wing_span)

    if oddness == "even":
        return True
    else:
        return False

# recursive function
# that calculates factorial numbers
def factorial(n):
    if n <= 2:
        return n
    else:
        n * factorial(n - 1)
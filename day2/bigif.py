grade = 92

# completa estas condiciones
if grade >= 90:
    print("A")
elif grade < 90 and grade >= 80:
    print("B")
elif grade < 80 and grade >= 70:
    print("C")
# if expresion then
# si expresion entonces
elif grade >= 60 and grade <= 69:
    print("D")
# elif grade <= 59 and grade > 39:
# elif grade >= 59.4:
elif grade <= 59 and grade >= 40:
    print("E")
else:
    print("F")
# else grade <= 59 grade >= 40:

# E es cuando 40 >= grade < 59
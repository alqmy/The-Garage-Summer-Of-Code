numero_de_notas = 0
promedio = 0.0

print("Cuantas notas tienes?")

numero_de_notas = int(input())

count = 0

while count != numero_de_notas:
    print("Entre nota en decimal")
    nota = float(input())
    promedio = promedio + nota

    count = count + 1


promedio = promedio / numero_de_notas

print("El promedio es")
print(promedio)
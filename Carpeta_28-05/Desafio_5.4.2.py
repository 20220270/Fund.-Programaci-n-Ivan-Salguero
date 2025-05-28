# Ejemplo 4.2

numero = 10
while True:
    print(numero)
    numero -=2
    if numero < 0:
        break

for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

# Desafio


# Genera un numero aleatorio entre el 1 y el 100, y pide al usuario que adivine el número. Por cada intento el programa informara si el numero que ingresa es mayor o menor al numero generado. El programa finaliza cuando el usuario adivina el numero o se rinde.

import random

numero_aleatorio = random.randint(1, 100)

numero_usuario = int(input("Adivina el número entre 1 y 100: "))

while numero_usuario != numero_aleatorio:
    if numero_usuario < numero_aleatorio:
        print("El número es mayor.")
    if numero_usuario > numero_aleatorio:
        print("El número es menor.")
    numero_usuario = int(input("Intenta nuevamente: "))
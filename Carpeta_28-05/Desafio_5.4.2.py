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

numero_aleatorio = random.randint(1, 100) # Aquí genero un numero random entre 1 y 100

numero_usuario = int(input("Adivina el número entre 1 y 100: "))

while numero_usuario != numero_aleatorio: # Mientras el usuario no adivine el número, seguimos pidiendo intentos
    if numero_usuario < numero_aleatorio: # Si el número del usuario es menor al número aleatorio, imprime "El número es mayor"
        print("El número es mayor.")
    if numero_usuario > numero_aleatorio: # Si el número del usuario es mayor al número aleatorio, imprime "El número es menor"
        print("El número es menor.")
    numero_usuario = int(input("Intenta nuevamente: "))

if numero_usuario == numero_aleatorio: # Si el usuario adivina el número, imprime un mensaje de felicitación
    print("¡Felicidades! Adivinaste el número.")
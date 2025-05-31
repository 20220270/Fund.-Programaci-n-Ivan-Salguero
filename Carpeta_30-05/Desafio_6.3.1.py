# Dada una lista de números ingresada por el usuario, imprime los numeros lideres de mayor a menor.

numeros = []  # Guardamos una lista para almacenar los números ingresados
while True:  # Mientras el usuario no ingrese "fin", seguimos pidiendo números
    entrada = input("Ingresa un número (o 'fin' para terminar): ")
    if entrada.lower() == "fin":  # Si el usuario ingresa "fin", salimos del bucle
        break
    try:
        numero = float(entrada)  # Convertimos la entrada a un número
        numeros.append(numero)  # Agregamos el número a la lista
    except ValueError:
        print("Por favor, ingresa un número válido o la palabra 'fin' para terminar.")

# Si el bucle termina, ordenamos la lista de números de mayor a menor
numeros_ordenados = sorted(numeros, reverse=True) # con sorted ordenamos unas lista de menor a mayor, con reverse=True la ordenamos de mayor a menor
print(f"La lista de números ordenada de mayor a menor es: {numeros_ordenados}")

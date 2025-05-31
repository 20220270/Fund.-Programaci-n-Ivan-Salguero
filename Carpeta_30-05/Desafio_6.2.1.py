# Dada una lista de números ingresada por el usuario, elimina los números duplicados y muestra la lista resultante.

numeros = []  # Guardamos una lista para almacenar los números ingresados
while True:  # Mientras el usuario no ingrese "fin", seguimos pidiendo números
    entrada = input("Ingresa un número (o 'fin' para terminar): ")
    if entrada.lower() == "fin":  # Si el usuario ingresa "fin", salimos del bucle
        break
    try:
        numero = float(entrada)  # Convertimos la entrada a un número
        if numero not in numeros:  # Solo agregamos el número si no está ya en la lista
            numeros.append(numero)
            print(f"Número {numero} agregado a la lista.")
        else:
            print(f"Número {numero} ya está en la lista, no se agrega.")
    except ValueError:
        print("Por favor, ingresa un número válido o la palabra 'fin' para terminar.")

# Si el bucle termina, mostramos la lista de números sin duplicados
print(f"La lista de números sin duplicados es: {numeros}")

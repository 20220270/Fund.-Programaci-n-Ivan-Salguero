# Dada una lista de números ingresada por el usuario, imprime su suma total.

numeros = [] # Guradmos una lista para almacenar los números ingresados
while True: # Mientras el usuario no ingrese "fin", seguimos pidiendo números
    entrada = input("Ingresa un número (o 'fin' para terminar): ")
    if entrada.lower() == "fin": # Si el usuario ingresa "fin", salimos del bucle
        break
    try:
        numero = float(entrada) # Convertimos la entrada a un número
        numeros.append(numero) # Agregamos el número a la lista
    except ValueError:
        print("Por favor, ingresa un número válido o la palabra 'fin' para terminar.")

suma_total = sum(numeros) # Si el bucle termina, calculamos la suma total de los números
print(f"La suma total de los números ingresados es: {suma_total}")
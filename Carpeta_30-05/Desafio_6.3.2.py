# Dada una lista circular de números ingresada por el usuario, determine cuantas rotaciones minimas a la izquierdas son necesarias para que esten en orden ascendente. En caso de que no se pueda, imprima -1.

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
# Si el bucle termina, verificamos si la lista es circular y ordenada
def rotaciones_minimas(lista):
    n = len(lista)
    lista_ordenada = sorted(lista)
    for i in range(n):
        rotada = lista[i:] + lista[:i]
        if rotada == lista_ordenada:
            return i
    return -1

rotaciones = rotaciones_minimas(numeros)
if rotaciones != -1:
    print(f"Las rotaciones mínimas a la izquierda necesarias para que la lista esté en orden ascendente son: {rotaciones}")
else:
    print("-1")

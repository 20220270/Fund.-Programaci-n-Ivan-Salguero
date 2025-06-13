#Comprobar si una matriz cuadrada es simétrica

# Qué debe cumplirse para que una matriz sea simétrica:
# - Debe ser cuadrada (mismo número de filas y columnas).
# - El elemento en la posición (i, j) debe ser igual al elemento en la posición (j, i) para todos los i y j.
def es_simetrica(matriz):
    n = len(matriz)
    for i in range(n):
        for j in range(i + 1, n):
            if matriz[i][j] != matriz[j][i]: # Si no son iguales, no es simétrica
                return False
    return True

# Pedir al usuario el tamaño de la matriz
n = int(input("Ingrese el tamaño de la matriz cuadrada: "))

# Crear la matriz vacía
matriz = []

# Llenar la matriz con los valores del usuario
print("Ingrese los elementos de la matriz fila por fila:")
for i in range(n):
    fila = input(f"Fila {i + 1} (ingrese {n} números separados por espacio): ").split()
    if len(fila) != n:
        print("Error: cada fila debe tener exactamente", n, "elementos.")
        exit()
    fila_numeros = [int(num) for num in fila]
    matriz.append(fila_numeros)

# Verificar si es simétrica
if es_simetrica(matriz):
    print("La matriz es simétrica")
else:
    print("La matriz no es simétrica")






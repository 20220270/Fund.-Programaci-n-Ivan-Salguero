#Comprobar si una matriz cuadrada es simétrica

# Qué debe cumplirse para que una matriz sea simétrica:
# - Debe ser cuadrada (mismo número de filas y columnas).
# - El elemento en la posición (i, j) debe ser igual al elemento en la posición (j, i) para todos los i y j.

# Pedimos al usuario el tamaño de la matriz
n = int(input("Ingrese el tamaño de la matriz cuadrada: "))

# Creamos la matriz vacía
matriz = []

def es_simetrica(matriz):
    n = len(matriz) #  Obtenemos el tamaño de la matriz
    for i in range(n): # Recorremos las filas
        for j in range(i + 1, n): # Recorremos las columnas, comenzando desde i + 1
            if matriz[i][j] != matriz[j][i]: # Si no son iguales, no es simétrica la matriz
                return False
    return True

# Llenar la matriz con los valores del usuario
print("Ingrese los elementos de la matriz fila por fila:")
for i in range(n):
    fila = input(f"Fila {i + 1} (ingrese {n} números separados por espacio): ").split()
    if len(fila) != n: # Si la longitud de la fila no es igual al tamaño ingresado, mostrar un error
        print("Error: cada fila debe tener exactamente", n, "elementos.")
        exit()
    fila_numeros = [int(num) for num in fila] # Convertir cada elementos de la fila a enteros
    matriz.append(fila_numeros) # Los agregamos a la matriz

# Verificar si es simétrica
if es_simetrica(matriz):
    print("La matriz es simétrica")
else:
    print("La matriz no es simétrica")






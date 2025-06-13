
n = int(input("Ingrese el tamaño de la matriz cuadrada (1, 2, 3, 4...): "))

# Inicializamos la matriz vacía
matriz = []

# Pedir al usuario que ingrese cada fila de la matriz
print("Ingrese los elementos fila por fila, separados por espacios:")
for i in range(n):
    fila = list(map(int, input(f"Fila {i+1}: ").split())) # Convertir la entrada en una lista de enteros
    if len(fila) != n: # Si la longitud de la fila no es igual al tamaño ingresado, mostrar un error
        print("Error: cada fila debe tener exactamente", n, "elementos.")
        exit()
    matriz.append(fila) # Sino, se agregará la fila a la matriz

# Inicializar listas para las diagonales
diagonal_principal = []
diagonal_secundaria = []

# Recorrer la matriz para extraer los elementos de las diagonales
for i in range(n): # Recorremos las filas
    for j in range(n):  # Recorremos las columnas
        if i == j: # Si el indice de fila es igual al índice de columna, es un elemento de la diagonal principal
            diagonal_principal.append(matriz[i][j])
        if i + j == n - 1: # Si la suma del índice de fila y columna es igual al tamaño de la matriz menos uno, es un elemento de la diagonal secundaria
            diagonal_secundaria.append(matriz[i][j])

# Mostrar las diagonales
print("Diagonal principal:", diagonal_principal)
print("Diagonal secundaria:", diagonal_secundaria)

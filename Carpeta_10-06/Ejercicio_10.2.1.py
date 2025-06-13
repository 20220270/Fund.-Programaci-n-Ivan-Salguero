
n = int(input("Ingrese el tamaño de la matriz cuadrada (1, 2, 3, 4...): "))

# Inicializar la matriz vacía
matriz = []

# Pedir al usuario que ingrese cada fila de la matriz
print("Ingrese los elementos fila por fila, separados por espacios:")
for i in range(n):
    fila = list(map(int, input(f"Fila {i+1}: ").split()))
    if len(fila) != n:
        print("Error: cada fila debe tener exactamente", n, "elementos.")
        exit()
    matriz.append(fila)

# Inicializar listas para las diagonales
diagonal_principal = []
diagonal_secundaria = []

# Recorrer la matriz para extraer los elementos de las diagonales
for i in range(n):
    for j in range(n):
        if i == j:
            diagonal_principal.append(matriz[i][j])
        if i + j == n - 1:
            diagonal_secundaria.append(matriz[i][j])

# Mostrar las diagonales
print("Diagonal principal:", diagonal_principal)
print("Diagonal secundaria:", diagonal_secundaria)

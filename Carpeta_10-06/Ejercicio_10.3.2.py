# Función para contar los vecinos con valor 1
def contar_vecinos(matriz, i, j, N, M):
    conteo = 0
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            if (0 <= x < N) and (0 <= y < M) and not (x == i and y == j):
                if matriz[x][y] == 1:
                    conteo += 1
    return conteo

# Dimensiones N y M de la matriz
N = int(input("Número de filas: "))
M = int(input("Número de columnas: "))


matriz = []
for i in range(N):
    entrada = input(f"Ingrese la fila {i + 1} con {M} valores separados por coma: ")
    elementos = entrada.split(",")
    fila = []
    for valor in elementos:
        fila.append(int(valor))
    matriz.append(fila)


# Crear nueva matriz con los conteos
resultado = []
for i in range(N):
    nueva_fila = []
    for j in range(M):
        vecinos = contar_vecinos(matriz, i, j, N, M)
        nueva_fila.append(vecinos)
    resultado.append(nueva_fila)

# Imprimir resultado
print("Salida:")
for fila in resultado:
    print(fila)

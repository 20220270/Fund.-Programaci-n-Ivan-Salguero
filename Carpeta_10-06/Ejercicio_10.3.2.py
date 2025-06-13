# Conteo de vecinos en una matriz


# Dimensiones N y M de la matriz
n = int(input("Número de filas: "))
m = int(input("Número de columnas: "))


matriz = []

# Función para contar los vecinos con valor 1
def contar_vecinos(matriz, i, j, N, M): # Parametros: matriz, fila i, columna j, número de filas N y número de columnas M
    conteo = 0
    for x in range(i-1, i+2): # Recorremos las filas vecinas
        for y in range(j-1, j+2):  # Recorremos las columnas vecinas
            if (0 <= x < N) and (0 <= y < M) and not (x == i and y == j): # Verificamos que los índices estén dentro de los límites de la matriz y que no sea el mismo elemento
                if matriz[x][y] == 1: # Si el vecino tiene valor 1, incrementamos el conteo
                    conteo += 1
    return conteo

for i in range(n): # Pedimos al usuario que ingrese cada fila de la matriz
    entrada = input(f"Ingrese la fila {i + 1} con {m} valores separados por espacios: ")
    elementos = entrada.split(" ")
    fila = []
    for valor in elementos:
        if valor != 0 or valor != 1: # Verificamos que los valores sean 0 o 1 ya que la matriz es binaria
            print("Error: los valores deben ser 0 o 1.")
            exit()
        fila.append(int(valor)) # Convertimos los valores a enteros debido a que la entrada es un string
    matriz.append(fila)


# Crear nueva matriz con los conteos
resultado = []
for i in range(n):
    nueva_fila = [] # Inicializamos una nueva fila para almacenar los conteos de vecinos
    for j in range(m):
        vecinos = contar_vecinos(matriz, i, j, n, m) # Contamos los vecinos de la posición (i, j)
        nueva_fila.append(vecinos)
    resultado.append(nueva_fila)

# Imprimir resultado
print("Salida:")
for fila in resultado:
    print(fila)

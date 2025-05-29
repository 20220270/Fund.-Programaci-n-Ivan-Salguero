# Dada una matriz 9x9 ingresada por el usuario, escribe un programa que compruebe si la matriz es un Sudoku válido.


def es_valido(grupo): # Comprobar si una fila, columna o subcuadro contiene los números del 1 al 9 y no deben repetirse
    return sorted(grupo) == list(range(1, 10)) # sorted(grupo) ordena el grupo y lo compara con una lista que contiene los números del 1 al 9. Si son iguales, devuelve True, de lo contrario, devuelve False.

def es_sudoku_valido(matriz):
    # Comprobamos filas i y columnas j, además de subcuadrículas 3x3
    for i in range(9):
        fila = matriz[i]
        columna = [matriz[j][i] for j in range(9)]
        if not es_valido(fila) or not es_valido(columna):
            return False

    # Comprobar subcuadrículas 3x3
    for f in range(0, 9, 3):
        for c in range(0, 9, 3):
            subcuadro = [matriz[i][j] for i in range(f, f+3) for j in range(c, c+3)]
            if not es_valido(subcuadro):
                return False

    return True

def ingresar_matriz(): # Función para ingresar una matriz 9x9
    print("Ingresa la matriz 9x9 (una fila por línea, separada por espacios):") # La matriz debe ser: un numero a la vez y separados por espacios
    matriz = []
    for i in range(9): # Iteramos 9 veces para ingresar las 9 filas
        fila = list(map(int, input(f"Fila {i+1}: ").split())) # Convertimos la entrada en una lista de enteros, 
        #además de separar los números por espacios y al final pasar a la siguiente fila
        if len(fila) != 9:
            raise ValueError("Cada fila debe contener exactamente 9 números.")
        matriz.append(fila)
    return matriz

# Ejecución
matriz = ingresar_matriz()

if es_sudoku_valido(matriz):
    print("Válido.")
else:
    print("Inválido.")

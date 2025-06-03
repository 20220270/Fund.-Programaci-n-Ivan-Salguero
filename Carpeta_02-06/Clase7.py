import numpy as np

# Ejemplos que nos da la guia
my_list = [1, 2, 3, 4, 5]
arr = np.array(my_list)
print(arr)

zeros = np.zeros((2, 3)) # Crea un arreglo de ceros de 2 filas y 3 columnas
print(zeros)

# Sumar arreglos
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr_sum  = arr1 + arr2 # [1 + 4, 2 + 5, 3 + 6]
print(arr_sum)

array1 = np.array([1, 2, 3])
array2 = np.array([[10], [20], [30]])

array_sum = array1 + array2  # Broadcasting: [1+10, 2+20, 3+30]
print(array_sum)  # Resultado: [[11], [22], [33]]

# Fin de ejemplos de la guia #

consumo = np.array([
    [12.5, 13.2, 11.9, 14.0, 13.5, 15.0, 14.3], # axis 1 evalúa en horizontal, axis 0 evalúa en vertical
    [10.1, 10.5, 10.0, 11.2, 11.5, 12.0, 11.8],
    [14.0, 14.2, 13.9, 15.5, 15.1, 16.0, 15.8],
    [9.0, 9.2, 8.9, 9.5, 9.8, 10.0, 9.7],
    [16.2, 16.5, 16.0, 17.1, 17.4, 5.0, 17.8],
    [11.0, 11.3, 11.1, 12.0, 12.4, 12.8, 12.5],
    [13.5, 13.8, 13.2, 14.1, 14.6, 15.0, 14.9],
    [10.8, 11.0, 10.6, 11.5, 11.8, 12.2, 12.0],
    [15.1, 15.5, 15.0, 16.0, 16.4, 17.0, 16.7],
    [8.5, 8.7, 8.4, 9.0, 9.2, 9.5, 9.3],
])

print("Dimensiones", consumo.ndim) # n dimensiones (2, filas y columnas)
print("Forma", consumo.shape) #  (10, 7) 10 filas y 7 columnas
print("Tipo de dato", consumo.dtype) # float64 
print("Consumo del primer hogar", consumo[0])
print("Consuma del miercoles (dia 3)", consumo[:, 2]) # Todas las filas, columna 2 (miércoles)

# Promedio de consumo por hogar a lo largo de la semana (la fila)
promedio_por_hogar = np.mean(consumo, axis = 1) # Axis = 1 promedia por fila

# Promedio de consumo diario de todos los hogares (la columna)
promedio_todos_hogares = np.mean(consumo, axis = 0) # Axis = 0 promedia por columna

# Suma total de consumo en la semana de los 10 hogares
suma_total = np.sum(consumo)

print("Promedio por hogar:", promedio_por_hogar)
print("Promedio diario de todos los hogares:", promedio_todos_hogares)
print("Suma total de consumo en la semana:", suma_total)

maximos = np.max(consumo, axis = 1)# Máximo consumo por hogar
minimos = np.min(consumo, axis = 0) # Mínimo consumo por día
desviacion = np.std(consumo) # desviación estandar global # Mide cúanto se dispersan los datos respecto a la media

# La desviación estandar se calcula como la raíz cuadrada de la varianza, 
# que es la media de las diferencias al cuadrado respecto a la media.

# Formula: # desviación estándar = sqrt(Σ((x_i - μ)²) / N)
# donde: la suma es sobre todos los elementos x_i, μ es la media y N es el número total de elementos.

print("Máximos por hogar:", maximos)
print("Mínimos por día:", minimos)
print("Desviación estándar global:", desviacion)

# Suma por hogar por semana
suma_por_hogar = np.sum(consumo, axis = 1)
# Encontrar el Índice del hogar con mayor consumo
hogar_mayor_consumo = np.argmax(suma_por_hogar)
total_mayor_consumo = np.max(maximos)
# Encontrar el Índice del hogar con menor consumo
hogar_menor_consumo = np.argmin(suma_por_hogar)
total_menor_consumo = np.min(minimos)
print("Suma por hogar:", suma_por_hogar)
print("Índice del hogar con mayor consumo:", hogar_mayor_consumo, "con un total de:", total_mayor_consumo)
print("Índice del hogar consumo:", hogar_menor_consumo, "con un total de:", total_menor_consumo)

# Suma de todos los hogares
suma_todos_hogares = np.sum(consumo, axis= 1)
print("Suma de todos los hogares:", suma_todos_hogares)

# Buscar solamente los hogares con consumo mayor a 100
altos = suma_todos_hogares > 100

consumo_mayor_100 = np.where(altos)[0] # Obtiene los índices de los hogares con consumo mayor a 100
print("Índices de hogares con consumo mayor a 100:", consumo_mayor_100)

# Consumo normalizado
consumo_normalizado = (consumo / consumo.min())/(consumo.max() - consumo.min())
print("Consumo normalizado:\n", consumo_normalizado)

# Cuestionario #/////////////////////////////////////////////////////////
# Consumo del hogar 5 el viernes, dia 5
consumo_quinto_viernes = consumo[4, 5] # Acceso al hogar 5 (índice 4) y al viernes (índice 5) # Domingo es indice 0, sabado es indice 7
print("Consumo del hogar 5 el viernes:", consumo_quinto_viernes)

# Usando indexacion, muestre el consumo de los ultimos 3 hogares el domingo (indice 0)
consumo_ultimos_tres_hogares = consumo[-3:, 0]
print("Consumo de los últimos 3 hogares el domingo:", consumo_ultimos_tres_hogares)

# Calcula el promedio de consumo los fines de semana (sábado y domingo, columnas 5 y 6).
fin_de_semana = consumo[:, 5:6]  # Selecciona las columnas de sábado y domingo
print("Promedio de consumo los fines de semana:", np.mean(fin_de_semana, axis=1))

# ¿Qué día de la semana tiene la mayor desviación estándar entre hogares? Explica qué indica esto.
desviaciones_por_dia = np.std(consumo, axis=0)  # Desviación estándar por días
dia_mayor_desviacion = np.argmax(desviaciones_por_dia)  # Índice del día con mayor desviación estándar
print("Día de la semana con mayor desviación estándar:", dia_mayor_desviacion)
# Explicación: Esto indica que en ese día, los hogares tienen un consumo más variable, lo que puede deberse a varios factores

#  Identifica los 3 hogares con menor consumo total durante la semana. Muestra sus índices y valores.
tres_hogares_menor_consumo = np.argsort(suma_por_hogar)[:3]  # Índices de los 3 hogares con menor consumo
print("Índices de los 3 hogares con menor consumo total:", tres_hogares_menor_consumo, "con valores:", suma_por_hogar[tres_hogares_menor_consumo])

# 6. Si el hogar 3 aumenta su consumo en un 10% cada día, ¿cuál sería su nuevo consumo total semanal?
nuevo_consumo_hogar_3 = consumo[2] * 1.10  # Aumenta el consumo del hogar 3 en un 10%
nuevo_total_hogar_3 = np.sum(nuevo_consumo_hogar_3)  # Suma el nuevo consumo semanal
print("Nuevo consumo total semanal del hogar 3:", nuevo_total_hogar_3)

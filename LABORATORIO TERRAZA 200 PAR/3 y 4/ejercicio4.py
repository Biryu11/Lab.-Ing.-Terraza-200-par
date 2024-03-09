# importar "numpy" al código

import numpy as np

def submatriz_mayor_suma(matriz):
   
    filas, columnas = matriz.shape
    max_suma = float('-inf')
    resultado = None

    for inicio_fila in range(filas):
        temp = np.zeros(columnas)
        for fin_fila in range(inicio_fila, filas):
            temp += matriz[fin_fila, :]
            max_temp = np.max(temp)
            if max_temp > max_suma:
                max_suma = max_temp
                resultado = matriz[inicio_fila:fin_fila+1, :]

    return resultado

# El ejemplo de uso
matriz_ejemplo = np.array([[1, 2, -1, 4],
                           [-8, -3, 4, 2],
                           [2, 8, 3, -6],
                           [5, 1, -1, 7]])

submatriz_max_suma = submatriz_mayor_suma(matriz_ejemplo)

# Imprimir los resultados

print("La Matriz: ")
print(matriz_ejemplo)

print("\nLa Submatriz de mayor suma es: ")
print(submatriz_max_suma)

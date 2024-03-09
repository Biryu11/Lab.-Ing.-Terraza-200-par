# importar "numpy" al código

import numpy as np

# Matriz 1 de tamaño 2x3
matriz1 = np.array([[1, 2, 3],
                    [4, 5, 6]])

# Matriz 2 de tamaño 2x2
matriz2 = np.array([[7, 8],
                    [9, 10]])

# Ajustar la dimensión de la Matriz 2 para que sea compatible con la Matriz 1
matriz2_ajustada = np.pad(matriz2, ((0, 0), (0, 1)), mode='constant', constant_values=0)

# Se suman los resultados de las matrices
resultado = matriz1 + matriz2_ajustada

# Se imprimen los resultados
print("Matriz 1: ")
print(matriz1)

print("\nMatriz 2 ajustada: ")
print(matriz2_ajustada)

print("\nEl resultado es: ")
print(resultado)

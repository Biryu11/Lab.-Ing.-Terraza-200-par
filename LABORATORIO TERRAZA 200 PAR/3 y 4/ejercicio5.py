# importar "numpy" al código

import numpy as np

def matriz_covarianza(matriz1, matriz2):
    
    covarianza = np.cov(matriz1, matriz2, rowvar=False)
    return covarianza

# El ejempo de uso
matriz1 = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

matriz2 = np.array([[9, 8, 7],
                    [6, 5, 4],
                    [3, 2, 1]])

matriz_cov = matriz_covarianza(matriz1, matriz2)

# Imprimir los resultados
print("Matriz 1:")
print(matriz1)

print("\nMatriz 2:")
print(matriz2)

print("\nMatriz de covarianza:")
print(matriz_cov)

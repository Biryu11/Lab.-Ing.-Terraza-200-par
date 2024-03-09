# importar "numpy" al código

import numpy as np

def encontrar_maximo(matriz):
   
    maximo = np.max(matriz)
    return maximo

# El ejemplo del uso es

matriz_ejemplo = np.array([[1, 5, 3],
                           [8, 2, 7],
                           [4, 9, 6]])

elemento_maximo = encontrar_maximo(matriz_ejemplo)

# Imprimir los resultados

print("La matriz: ")
print(matriz_ejemplo)

print("\nEl elemento maximo de la matriz es: ", elemento_maximo)

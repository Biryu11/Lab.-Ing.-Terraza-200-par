# importar "numpy" al código

import numpy as np

# Definir una matriz de ejemplo
matriz = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Calcular la media, mediana y desviación estándar de los elementos de la matriz
media = np.mean(matriz)
mediana = np.median(matriz)
desviacion_estandar = np.std(matriz)

# Imprimir la matriz y los resultados
print("Matriz:")
print(matriz)

print("\nLa Media de los elementos de la matriz es: ", media)

print("La Mediana de los elementos de la matriz es: ", mediana)

print("La desviacion estandar de los elementos de la matriz es:", desviacion_estandar)

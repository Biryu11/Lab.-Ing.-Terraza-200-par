# Importamos numpy para las matrices
import numpy as np

# se crea una matriz de ejemplo, es este caso una de 3x3
matriz = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# se calcula para sacar el elemento central
filas, columnas = matriz.shape
Fila_Central, Columna_Central = filas // 2, columnas // 2

# se accede al elemento central
EleCen = matriz[Fila_Central, Columna_Central]

# se imprime el resultado con "print"
print("El elemento central de la matriz es: ", EleCen)

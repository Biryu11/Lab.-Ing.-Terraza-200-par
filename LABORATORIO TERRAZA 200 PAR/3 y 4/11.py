# importar "numpy" al código

import numpy as np

# se define una matriz de ejemplo
matriz = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

#el numero por el cual se multiplica la matriz
numero = 2

# Multiplicar la matriz por el número
resultado = numero * matriz

# Imprimir la matriz original y el resultado
print("Matriz original: ")
print(matriz)

print("\nEl resultado de la multiplicacion por", numero, "es :")
print(resultado)

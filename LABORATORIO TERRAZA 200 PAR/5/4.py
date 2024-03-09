def numeros_comunes(conjunto1, conjunto2):
    numeros_en_comun = conjunto1.intersection(conjunto2)
    return numeros_en_comun

conjunto_a = {2, 4, 6, 8, 10, 11, 18, 90}
conjunto_b = {5, 8, 10, 12, 15, 89, 88}
numeros_en_comun = numeros_comunes(conjunto_a, conjunto_b)

print(f"Conjunto A: {conjunto_a}")
print(f"Conjunto B: {conjunto_b}")
print(f"Números en común: {numeros_en_comun}")
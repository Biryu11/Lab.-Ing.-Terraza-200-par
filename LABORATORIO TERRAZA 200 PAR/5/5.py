def diferencia_entre_conjuntos(conjunto_1, conjunto_2):
    diferencia = conjunto_1.difference(conjunto_2)
    return diferencia

conj_a = {1, 5, 12, 8, 10, 9}
conj_b = {1, 8, 10, 12, 15, 20}
diferencia = diferencia_entre_conjuntos(conj_a, conj_b)

print(f"Conjunto A: {conj_a}")
print(f"Conjunto B: {conj_b}")
print(f"Números en el primero pero no en el segundo: {diferencia}")
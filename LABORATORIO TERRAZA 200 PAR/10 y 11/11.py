pila_original = [1, 2, 3, 2, 4, 3, 5]

pila_sin_duplicados = []
elementos_unicos = set()

while pila_original:
    elemento = pila_original.pop()

    if elemento not in elementos_unicos:
        pila_sin_duplicados.append(elemento)
        elementos_unicos.add(elemento)

pila_sin_duplicados.reverse()

print("La Pila original es: ", pila_original)
print("La Pila sin duplicados: ", pila_sin_duplicados)


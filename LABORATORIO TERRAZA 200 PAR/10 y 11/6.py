cadena_original = "Quiero una hamburguesa"

pila = list(cadena_original)

cadena_invertida = ""
while len(pila) > 0:
    cadena_invertida += pila.pop()

print("La Cadena original es: ", cadena_original)

print("La Cadena invertida es: ", cadena_invertida)

conjunto = {"manzana", "platano", "limon", "auto", "html", "negro"}

letra_buscar = 'a'

palabra_letra = set(filter(lambda palabra: letra_buscar in palabra, conjunto))

print("El conjunto original es: ", conjunto)
print(f"Palabras que contienen '{letra_buscar}':", palabra_letra)

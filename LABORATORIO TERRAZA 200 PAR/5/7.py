conjunto_palabras = {"amor", "roma", "hola", "aloh", "gato", "toga", "Pan", "navidad"}
palabras_ordenadas = {}
anagramas = set()

for palabra in conjunto_palabras:
    palabra_ordenada = ''.join(sorted(palabra))
    if palabra_ordenada in palabras_ordenadas:
        palabras_ordenadas[palabra_ordenada].add(palabra)
    else:
        palabras_ordenadas[palabra_ordenada] = {palabra}

for conjunto in palabras_ordenadas.values():
    if len(conjunto) > 1:
        anagramas.update(conjunto)

print("Anagramas encontrados:", anagramas)

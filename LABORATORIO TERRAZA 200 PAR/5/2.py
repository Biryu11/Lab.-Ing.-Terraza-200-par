def palabras_empiezan_con_letra(conjunto_palabras, letra):
    palabras_seleccionadas = {palabra for palabra in conjunto_palabras if palabra.startswith(letra)}
    return palabras_seleccionadas

palabras = {"cupid", "pez", "dolar", "hogar", "tiempo"}
letra = input("Ingrese la letra para ver las palabras que empiezan con esta: ")
palabras_filtradas = palabras_empiezan_con_letra(palabras, letra)

print("Palabras: ", palabras)
print("Palabras que comienzan con ", letra, ": ", palabras_filtradas)
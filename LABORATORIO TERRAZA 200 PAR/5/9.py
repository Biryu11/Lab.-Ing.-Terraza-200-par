def palabras_con_longitud(conjunto_palabras, longitud):
    palabras_seleccionadas = {palabra for palabra in conjunto_palabras if len(palabra) == longitud}
    return palabras_seleccionadas

palabras = {"pecera", "mesa", "silla", "juegos", "mañana"}
longitud_deseada = 6
palabras_seleccionadas = palabras_con_longitud(palabras, longitud_deseada)

print(f"Palabras originales: {palabras}")
print(f"Palabras con longitud {longitud_deseada}: {palabras_seleccionadas}")
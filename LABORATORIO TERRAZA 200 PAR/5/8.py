def obtener_palindromos(conjunto_de_palabras):
    palindromos = {palabra for palabra in conjunto_de_palabras if palabra == palabra[::-1]}
    return palindromos

palabras = {"ana", "pecera", "mesa", "radar"}
palindromos = obtener_palindromos(palabras)

print(f"Palabras originales: {palabras}")
print(f"Palíndromos: {palindromos}")
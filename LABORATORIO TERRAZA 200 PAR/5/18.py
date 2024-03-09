conjunto = {"hola", "casa", "programacion", "lengua", "palindromo", "musica", "conjunto", "Mesa"}
letra = "o"
palabras = sorted([x for x in conjunto if letra in x], reverse=True)

print("El conjunto original es: ", conjunto)
print("el conjunto con ciertas palabras es: ", palabras)

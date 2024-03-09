conjunto = {"python", "java", "csharp", "javascript", "html", "css"}
longitud = 4

resultado = set(sorted({palabra for palabra in conjunto if len(palabra) == longitud}))

print("el conjunto original:", conjunto)
print(f"Las palabras de longitud {longitud} ordenadas es:", resultado)

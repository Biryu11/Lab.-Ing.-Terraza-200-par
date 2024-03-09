ejemplo = "Hola a todos"

contar_vocales = sum(1 for char in ejemplo.lower() if char in "aeiou")

print("El numero de vocales en la cadena es: ", contar_vocales)
palabra = input("Ingresa la palabra: ").lower()
palabra = "".join(c for c in palabra if c.isalnum())

print(f"{palabra} {'es' if palabra == palabra[::-1] else 'no es'} un palíndromo")
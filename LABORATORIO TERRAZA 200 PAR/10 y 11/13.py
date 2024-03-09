def limpiar_cadena(cadena):
    return ''.join(c.lower() for c in cadena if c.isalnum())

def es_palindromo(cadena):
    cadena_limpia = limpiar_cadena(cadena)
    
    pila = []

    for char in cadena_limpia[:len(cadena_limpia)//2]:
        pila.append(char)

    start = len(cadena_limpia)//2 + len(cadena_limpia) % 2

    for char in cadena_limpia[start:]:
        if not pila or pila.pop() != char:
            return False

    return True

palabra = "anita lava la tina"
if es_palindromo(palabra):
    print(f'"{palabra}" es un palíndromo.')
else:
    print(f'"{palabra}" no es un palíndromo.')


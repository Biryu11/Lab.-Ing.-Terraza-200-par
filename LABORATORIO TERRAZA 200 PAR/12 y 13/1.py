from collections import deque

def es_palindromo(palabra):
    cola = deque()
    for letra in palabra:
        cola.append(letra)
    
    es_palindromo = True
    while len(cola) > 1 and es_palindromo:
        primera_letra = cola.popleft()
        ultima_letra = cola.pop()
        if primera_letra != ultima_letra:
            es_palindromo = False
    
    return es_palindromo

palabra = "reconocer"
if es_palindromo(palabra):
    print(f"{palabra} es un palíndromo")
else:
    print(f"{palabra} no es un palíndromo")

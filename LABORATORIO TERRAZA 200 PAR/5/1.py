def obtener_primos(conjunto):
    primos = set()
    for numero in conjunto:
        if es_primo(numero):
            primos.add(numero)
    return primos


def es_primo(numero):
    cont = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            cont += 1
    if cont == 2:
        return True
    else:
        return False

numeros = {2, 3, 5, 9}
primos = obtener_primos(numeros)
print("Números originales:", numeros)
print("Números primos:", primos)
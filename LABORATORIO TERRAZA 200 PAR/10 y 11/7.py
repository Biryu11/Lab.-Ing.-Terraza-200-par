numero_decimal = int(input("Ingrese el número decimal: "))

pila = []

while numero_decimal > 0:
    residuo = numero_decimal % 2
    pila.append(residuo)
    numero_decimal //= 2

binario = ""
while len(pila) > 0:
    binario += str(pila.pop())

print(f"En binarios seria es: {binario}")

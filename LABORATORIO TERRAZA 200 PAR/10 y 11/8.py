expresion_posfija = ["2", "4", "*", "5", "+"]

pila = []

for token in expresion_posfija:
    if token.isdigit():

        pila.append(int(token))

    else:
        operando2 = pila.pop()
        operando1 = pila.pop()

        if token == "+":
            resultado = operando1 + operando2
        elif token == "-":
            resultado = operando1 - operando2
        elif token == "*":
            resultado = operando1 * operando2
        elif token == "/":
            resultado = operando1 / operando2  

        pila.append(resultado)

resultado_final = pila.pop()

print(f"El resultado es: {resultado_final}")


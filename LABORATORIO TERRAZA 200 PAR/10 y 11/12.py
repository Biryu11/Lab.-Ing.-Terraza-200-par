expresion = "3 + 5 * (4 - 2)"

pila = []
operadores = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x / y}

for token in expresion.split():
    if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
        pila.append(float(token))
    elif token in operadores:
        operando2, operando1 = pila.pop(), pila.pop()
        pila.append(operadores[token](operando1, operando2))

resultado = pila[0] if len(pila) == 1 else None
print("Resultado:", resultado) if resultado is not None else print("Error: Expresión no válida.")

def validar_operadores_anidados(expresion):
    pila = []

    operadores_validos = {"(": ")", "[": "]", "{": "}"}

    for caracter in expresion:
        if caracter in operadores_validos.keys():
            pila.append(caracter)
        elif caracter in operadores_validos.values():
            if not pila or operadores_validos[pila.pop()] != caracter:
                return False  
    return not pila

expresion_valida = "{(2 + 3) * [4 - 1]}"
expresion_invalida = "{(2 + 3) * [4 - 1}"

if validar_operadores_anidados(expresion_valida):
    print("La expresión es válida.")
else:
    print("La expresión no es válida.")

if validar_operadores_anidados(expresion_invalida):
    print("La expresión es válida.")
else:
    print("La expresión no es válida.")

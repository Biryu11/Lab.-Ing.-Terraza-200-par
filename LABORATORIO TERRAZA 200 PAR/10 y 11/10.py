def ordenar_pila(pila):
    pila_ordenada = []  
    while pila:
        elemento = pila.pop()

        while pila_ordenada and pila_ordenada[-1] > elemento:
            pila.append(pila_ordenada.pop())

        pila_ordenada.append(elemento)

    return pila_ordenada

pila_desordenada = [4, 2, 8, 1, 5]

print("La Pila original es: ", pila_desordenada)

pila_ordenada = ordenar_pila(pila_desordenada)

print("La Pila ordenada es: ", pila_ordenada)

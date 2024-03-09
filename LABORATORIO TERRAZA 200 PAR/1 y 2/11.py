lista_numeros = [float(x) for x in input("Ingresa una lista de números: ").split()]

lista_numeros_ordenada = sorted(lista_numeros)
lista_numeros_ordenada = [int(x) if x.is_integer() else x for x in lista_numeros_ordenada]


print("la lista ordenada de menor a mayor es:", lista_numeros_ordenada)

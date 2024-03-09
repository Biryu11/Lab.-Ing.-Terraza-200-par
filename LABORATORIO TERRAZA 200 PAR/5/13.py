conjunto = {1, 2, 3, 2, 3, 2, 4, 5, 6, 3, 7, 8, 9, 1}

duplicados = set(filter(lambda x: list(conjunto).count(x) > 1, conjunto))

print("el conjunto original es: ", conjunto)
print("el conjunto de números duplicados es: ", duplicados)

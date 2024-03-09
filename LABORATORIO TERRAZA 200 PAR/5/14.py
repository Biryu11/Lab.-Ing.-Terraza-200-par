conjunto = {1, 2, 2, 3, 4, 4, 5}
no_duplicados = set([x for x in conjunto if list(conjunto).count(x) == 1])

print("El conjunto original es: ", conjunto)
print("El conjunto de no duplicados es: ", no_duplicados)

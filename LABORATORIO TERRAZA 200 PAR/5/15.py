conjunto = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
no_duplicados = set([x for x in conjunto if all(x % y != 0 for y in range(2, int(x**0.5)+1))])
no_duplicados = sorted(no_duplicados)

print("El conjunto original es: ", conjunto)
print("El conjunto de no duplicados es: ", no_duplicados)


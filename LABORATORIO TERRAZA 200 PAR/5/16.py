conjunto = {"reconocer", "oso", "casa", "radar", "solos", "somos", "luz azul"}
palindromos = sorted([x for x in conjunto if x == x[::-1]])

print("El conjunto original es: ", conjunto)
print("El conjunto de palindromos es: ", palindromos)

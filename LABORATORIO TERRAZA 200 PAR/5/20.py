conjunto = {"reconocer", "oso", "casa", "radar", "solos", "somos", "luz azul"}
longitud = 5
palindromos = sorted([x for x in conjunto if x == x[::-1] and len(x) == longitud])

print("El conjunto original es: ", conjunto)
print("El conjunto de palindromos con limite definido es: ", palindromos)

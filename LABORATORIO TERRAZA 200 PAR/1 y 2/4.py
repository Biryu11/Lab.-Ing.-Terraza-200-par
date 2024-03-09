def factorial(n):
    resultado = 1
    for i in range(1, n+1):
        resultado *= i
    return resultado

numero = int(input("Ingresa un número: "))
factorial_numero = factorial(numero)
print("El factorial de", numero, "es", factorial_numero)

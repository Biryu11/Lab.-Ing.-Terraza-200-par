numero = int(input("Ingresa un numero entero: "))
suma_digitos = sum(int(digito) for digito in str(abs(numero)))


print(f"La suma de los dígitos de {numero} es {suma_digitos} ")


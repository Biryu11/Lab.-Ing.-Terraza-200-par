inicio = int(input("Ingrese el inicio del rango: "))
fin = int(input("Ingrese el final del rango: "))

suma_pares = sum(numero for numero in range(inicio, fin + 1) if numero % 2 == 0)

print(f"La suma de los números pares en el rango de {inicio} a {fin} es: {suma_pares}")

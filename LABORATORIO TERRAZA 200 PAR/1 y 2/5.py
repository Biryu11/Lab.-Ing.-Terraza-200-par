numero = int(input("Ingresa numerin: "))
contador = 0
for i in range(1,numero + 1):
    if numero % i == 0:
        contador += 1
if contador == 2:
    print("Es primo")
else:
    print("No es primo")
numero = int(input("Ingrese un numero: "))
print(" I", end = '')
for j in range(1, numero + 1):
	print("  ", j, end = '')
print()
print("__________")

for i in range(1, numero + 1):
	print(i, "I", end = '')
	for j in range(1, numero + 1):
		print(format(i * j, "4d"), end = '')
	print()
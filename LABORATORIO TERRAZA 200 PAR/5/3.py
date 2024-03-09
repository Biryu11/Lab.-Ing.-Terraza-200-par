def numeros_divisibles(conjunto_numeros, divisor):
    numeros_seleccionados = {n for n in conjunto_numeros if n % divisor == 0}
    return numeros_seleccionados

numeros = {2, 4, 7, 8, 15, 16}
divisor_deseado = int(input(("Ingresar el número a dividir: ")))
numeros_divisibles_por_cinco = numeros_divisibles(numeros, divisor_deseado)

print("Números originales: ", numeros)
print("Números divisibles por ", divisor_deseado, ": ", numeros_divisibles_por_cinco)
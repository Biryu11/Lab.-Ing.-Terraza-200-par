def suma(a, b):
    resultado = a + b
    return resultado

resultado_calculado = suma(2, 3)

assert resultado_calculado == 5, f"La función suma debería retornar 5, pero retornó {resultado_calculado}"

print("La función suma retorna el valor esperado")

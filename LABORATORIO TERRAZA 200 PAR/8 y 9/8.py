# Definir una clase simple
class Contador:
    def __init__(self):
        self.valor = 0

    def incrementar(self):
        self.valor += 1

El_contador = Contador()

El_contador.incrementar()

assert El_contador.valor == 1, f"El valor del contador debería ser 1, pero es {El_contador.valor}"

print("Se ha dejado en el estado esperado")

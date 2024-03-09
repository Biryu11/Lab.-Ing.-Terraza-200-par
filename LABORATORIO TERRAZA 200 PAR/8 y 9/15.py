class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazadaSimple:
    def __init__(self):
        self.inicio = None

    def agregar_nodo(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.inicio
        self.inicio = nuevo_nodo

    def imprimir_lista(self):
        actual = self.inicio
        while actual is not None:
            print(actual.dato, end=" ")
            actual = actual.siguiente
        print()

    def invertir_lista(self):
        actual = self.inicio
        anterior = None

        while actual is not None:
            siguiente_nodo = actual.siguiente
            actual.siguiente = anterior
            anterior = actual
            actual = siguiente_nodo

        self.inicio = anterior

# Ejemplo de uso
lista = ListaEnlazadaSimple()
lista.agregar_nodo(1)
lista.agregar_nodo(2)
lista.agregar_nodo(3)
lista.agregar_nodo(4)

print("La lista original es: ")
lista.imprimir_lista()

lista.invertir_lista()

print("La lista invertida es: ")
lista.imprimir_lista()







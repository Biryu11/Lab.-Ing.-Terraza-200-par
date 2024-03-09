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

    def eliminar_duplicados(self):
        if self.inicio is None or self.inicio.siguiente is None:
            return self.inicio
    
        unicos = set()
        actual = self.inicio
        unicos.add(actual.dato)

        while actual.siguiente is not None:
            if actual.siguiente.dato in unicos:
                actual.siguiente = actual.siguiente.siguiente
            else:
                unicos.add(actual.siguiente.dato)
                actual = actual.siguiente

    def longitud_de_lista(self):
        longitud = 0
        actual = self.inicio

        while actual is not None:
            longitud += 1
            actual = actual.siguiente

        return longitud

    def imprimir_lista(self):
        actual = self.inicio
        while actual is not None:
            print(actual.dato, end=" ")
            actual = actual.siguiente
        print()

# Ejemplo de uso
lista_enlazada = ListaEnlazadaSimple()
lista_enlazada.agregar_nodo(1)
lista_enlazada.agregar_nodo(2)
lista_enlazada.agregar_nodo(3)

longitud = lista_enlazada.longitud_de_lista()

print("La longitud de la lista es:", longitud)



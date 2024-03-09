# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 20:54:22 2024

@author: Lenovo
"""

# Buscar un módulo

class Nodo:
    def __init__(self, modulo, siguiente=None):
        self.modulo = modulo
        self.siguiente = siguiente

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_nodo(self, modulo):
        nuevo_nodo = Nodo(modulo)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def buscar_modulo(self, modulo_buscado):
        nodo_actual = self.cabeza

        while nodo_actual is not None:
            if nodo_actual.modulo == modulo_buscado:
                return True  
            nodo_actual = nodo_actual.siguiente

        return False 

lista_enlazada = ListaEnlazada()
lista_enlazada.agregar_nodo(1)
lista_enlazada.agregar_nodo(2)
lista_enlazada.agregar_nodo(3)

# Buscar un módulo en la lista
modulo_buscado = 2
resultado = lista_enlazada.buscar_modulo(modulo_buscado)

if resultado:
    print(f"El módulo {modulo_buscado} está en la lista.")
else:
    print(f"El módulo {modulo_buscado} no está en la lista.")

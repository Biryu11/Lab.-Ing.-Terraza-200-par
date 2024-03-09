# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 20:57:29 2024

@author: Lenovo
"""

# Concatenar listas

class Nodo:
    def __init__(self, valor, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_nodo(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def concatenar_listas(self, otra_lista):
        if self.cabeza is None:
            self.cabeza = otra_lista.cabeza
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente is not None:
                nodo_actual = nodo_actual.siguiente
            
            nodo_actual.siguiente = otra_lista.cabeza

lista1 = ListaEnlazada()
lista1.agregar_nodo(3)
lista1.agregar_nodo(7)

lista2 = ListaEnlazada()
lista2.agregar_nodo(5)
lista2.agregar_nodo(9)

lista1.concatenar_listas(lista2)

nodo_actual = lista1.cabeza
while nodo_actual is not None:
    print(nodo_actual.valor, end=" ")
    nodo_actual = nodo_actual.siguiente

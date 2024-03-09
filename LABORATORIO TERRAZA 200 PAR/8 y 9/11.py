# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 20:56:19 2024

@author: Lenovo
"""

#Sumar los elementos de una lista enlazada

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

    def sumar_elementos(self):
        suma = 0
        nodo_actual = self.cabeza

        while nodo_actual is not None:
            suma += nodo_actual.valor
            nodo_actual = nodo_actual.siguiente

        return suma

lista_enlazada = ListaEnlazada()
lista_enlazada.agregar_nodo(3)
lista_enlazada.agregar_nodo(7)
lista_enlazada.agregar_nodo(5)

resultado_suma = lista_enlazada.sumar_elementos()
print(f"La suma de los elementos es: {resultado_suma}")

# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 19:50:27 2024

@author: Lenovo
"""

# Invertir la lista

class NodoDoble:
    def __init__(self, valor):
        self.valor= valor
        self.siguiente= None
        self.anterior= None
        
class ListaEnlazadaDoble:
    def __init__(self):
        self.primero= None
        self.fin= None
        
    def agregar_nodo(self, valor):
        nuevo_nodo= NodoDoble(valor)
        if not self.primero:
            self.primero= nuevo_nodo
            self.fin= nuevo_nodo
            
        else:
            nuevo_nodo.anterior= self.fin
            self.fin.siguiente= nuevo_nodo
            self.fin= nuevo_nodo
            
    def invertir_lista(self):
        actual= self.primero
        
        while actual:
            actual.siguiente, actual.anterior= actual.anterior, actual.siguiente
            actual= actual.anterior
            
        self.primero, self.fin = self.fin, self.primero
            
    def imprimir_hacia_adelante(self):
        actual= self.primero
        while actual:
            print(actual.valor, end=" ")
            actual= actual.siguiente
        print()
        
    def imprimir_hacia_atras(self):
        actual= self.fin
        while actual:
            print(actual.valor, end= " ")
            actual= actual.anterior
        print()
        
lista= ListaEnlazadaDoble()

for valor in [1,2,3,4,5]:
    lista.agregar_nodo(valor)
    
print("Lista original hacia adelante: ")
lista.imprimir_hacia_adelante()

print("Lista original hacia atrás: ")
lista.imprimir_hacia_atras()

lista.invertir_lista()

print("Lista invertida hacia adelante: ")
lista.imprimir_hacia_adelante()

print("Lista invertida hacia atrás: ")
lista.imprimir_hacia_atras()
                

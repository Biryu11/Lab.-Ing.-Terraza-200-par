# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 19:15:39 2024

@author: Lenovo
"""

# Duplicar nodos

class NodoDoble:
    def __init__(self, valor):
        self.valor= valor
        self.siguiente= None
        self.anterior= None
        
class ListaEnlazadaDoble:
    def __init__(self):
        self.primero= None
        self.ultimo= None
        
    def agregar_nodo(self, valor):
        nuevo_nodo= NodoDoble(valor)
        if not self.primero:
            self.primero= nuevo_nodo
            self.ultimo= nuevo_nodo
            
        else:
            nuevo_nodo.anterior= self.ultimo
            self.ultimo.siguiente= nuevo_nodo
            self.ultimo= nuevo_nodo
            
    def duplicar_nodos(self):
        actual= self.primero
        
        while actual:
            nuevo_nodo= NodoDoble(actual.valor)
            nuevo_nodo.anterior= actual
            nuevo_nodo.siguiente= actual.siguiente
            actual.siguiente= nuevo_nodo
            
            if nuevo_nodo.siguiente:
                nuevo_nodo.siguiente.anterior= nuevo_nodo
                
            actual= nuevo_nodo.siguiente
            
    def imprimir_hacia_adelante(self):
        actual= self.primero
        while actual:
            print(actual.valor, end=" ")
            actual= actual.siguiente
        print()
        
    def imprimir_hacia_atras(self):
        actual= self.ultimo
        while actual:
            print(actual.valor, end= " ")
            actual= actual.anterior
        print()
        
lista_original= ListaEnlazadaDoble()
for valor in [3,4,7,10]:
    lista_original.agregar_nodo(valor)
    
print("Lista original hacia adelante: ")
lista_original.imprimir_hacia_adelante()

print("Lista original hacia atrás: ")
lista_original.imprimir_hacia_atras()

lista_original.duplicar_nodos()

print("Lista duplicada hacia adelante: ")
lista_original.imprimir_hacia_adelante()

print("Lista duplicada hacia atrás: ")
lista_original.imprimir_hacia_atras()
                
                
                
                
                
                
                
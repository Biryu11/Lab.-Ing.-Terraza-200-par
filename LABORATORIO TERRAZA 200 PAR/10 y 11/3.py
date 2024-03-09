# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 19:37:27 2024

@author: Lenovo
"""

# Insertar nodo en posición específica

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
            
    def insertar_nodo_en_posicion(self, valor, posicion):
        nuevo_nodo = NodoDoble(valor)
        actual= self.primero
        contador= 1
        
        if posicion == 1:
            nuevo_nodo.siguiente= actual
            actual.anterior= nuevo_nodo
            
        else:
            while actual and contador < posicion -1:
                actual= actual.siguiente
                contador += 1
                
            if not actual:
                print("Posición no válida, la lista no es lo suficientemente larga")
                return
            
            nuevo_nodo.siguiente= actual.siguiente
            nuevo_nodo.anterior= actual
            if actual.siguiente:
                actual.siguiente.anterior= nuevo_nodo
            actual.siguiente= nuevo_nodo
            
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

for valor in [3, 4, 7, 12, 1]:
    lista.agregar_nodo(valor)
    
print("Lista original hacia adelante: ")
lista.imprimir_hacia_adelante()

print("Lista original hacia atrás: ")
lista.imprimir_hacia_atras()

lista.insertar_nodo_en_posicion(15, 3)

print("Lista con nuevo nodo hacia adelante: ")
lista.imprimir_hacia_adelante()

print("Lista con nuevo nodo hacia atrás: ")
lista.imprimir_hacia_atras()
                
                
                
                
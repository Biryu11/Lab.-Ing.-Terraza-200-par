# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 19:30:22 2024

@author: Lenovo
"""

# contar nodos pares e impares

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
            
    def contar_pares_impares(self):
        actual= self.primero
        pares= impares= 0
        
        while actual:
            if actual.valor % 2 == 0:
                pares += 1
                
            else:
                impares += 1
            actual= actual.siguiente
            
        return pares, impares
            
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

for valor in [5,4,22,6,3,8,10,12,13]:
    lista.agregar_nodo(valor)
    
print("Lista original hacia adelante: ")
lista.imprimir_hacia_adelante()

print("Lista original hacia atrás: ")
lista.imprimir_hacia_atras()

pares, impares= lista.contar_pares_impares()
print(f"Nodos con dato par: {pares}")
print(f"Nodos con dato impar: {impares}")
                
                
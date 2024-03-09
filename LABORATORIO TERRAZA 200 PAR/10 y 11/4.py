# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 19:45:09 2024

@author: Lenovo
"""
# Eliminar nodos duplicados

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
            
    def eliminar_nodos_duplicados(self):
        valores_vistos= set()
        actual= self.primero
        
        while actual:
            if actual.valor not in valores_vistos:
                valores_vistos.add(actual.valor)
                
            else:
                actual.anterior.siguiente= actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior= actual.anterior
                
                else:
                    self.fin= actual.anterior
                    
            actual= actual.siguiente
            
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

for valor in [2,2,3,4,2,6,5,8,7,7]:
    lista.agregar_nodo(valor)
    
print("Lista original hacia adelante: ")
lista.imprimir_hacia_adelante()

print("Lista original hacia atrás: ")
lista.imprimir_hacia_atras()

lista.eliminar_nodos_duplicados()

print("Lista sin nodos duplicados hacia adelante: ")
lista.imprimir_hacia_adelante()

print("Lista sin nodos duplicados hacia atrás: ")
lista.imprimir_hacia_atras()
                

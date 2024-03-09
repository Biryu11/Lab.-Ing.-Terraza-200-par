# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 18:58:30 2024

@author: Lenovo
"""

def imprimir_piramide(n, fila=1):
    if fila > n:
        return
    
    for i in range(1, fila + 1):
        print(i, end=" ")
    
    print()

    imprimir_piramide(n, fila + 1)

n = int(input("Ingresa un número: "))

imprimir_piramide(n)

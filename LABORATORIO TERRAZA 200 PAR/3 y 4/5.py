# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 19:05:15 2024

@author: Lenovo
"""

def imprimir_tabla(n, multiplicador= 1):
    
    if multiplicador <= 10:
        resultado= n*multiplicador
        print(n, " x ",multiplicador, "= ", resultado)
        
        imprimir_tabla(n, multiplicador + 1)
        
n= 5
imprimir_tabla(n)
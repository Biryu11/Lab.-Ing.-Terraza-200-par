# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 19:01:11 2024

@author: Lenovo
"""

def imprimir_piramide_inv(filas, actual= 1):
    if filas >0:
        espacios= " "*1
        
        for i in range(actual,0,-1):
            print(espacios+ str(i), end= " ")
            
        print()
        
        imprimir_piramide_inv(filas -1, actual +1)
        
n= 10
imprimir_piramide_inv(n)

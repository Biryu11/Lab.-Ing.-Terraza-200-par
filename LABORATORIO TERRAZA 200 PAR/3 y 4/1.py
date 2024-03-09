# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 18:31:33 2024

@author: Lenovo
"""

def imprimir_pares(numero):
    if numero <= 100:
        if numero % 2 == 0:
            print(numero)
        imprimir_pares(numero + 1)

# Llamamos a la función con el primer número para iniciar la recursión
imprimir_pares(1)

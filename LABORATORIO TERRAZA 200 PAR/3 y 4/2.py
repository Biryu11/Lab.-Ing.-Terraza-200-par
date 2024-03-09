# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 18:54:27 2024

@author: Lenovo
"""

def suma_recursiva(n):
    if n == 1:
        return 1
    else:
        return n + suma_recursiva(n - 1)

n = int(input("Ingresa un número entero positivo: "))

if n <= 0:
    print("Ingresa un número:")
else:
    resultado = suma_recursiva(n)
    print(f"La suma de los números del 1 al {n} es: {resultado}")

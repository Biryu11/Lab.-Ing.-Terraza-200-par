# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 20:10:21 2024

@author: Lenovo
"""

def verificar_edad(edad):
    
    assert edad.isdigit(), "La edad debe ser un número entero positivo"
    assert int(edad) > 0 or edad.isdigit(), "La edad debe ser un número entero positivo"

    print(f"Edad verificada: {int(edad)}")

edad_ingresada = input("Ingresa tu edad: ")

try:
    verificar_edad(edad_ingresada)
except AssertionError as e:
    print(f"Error: {e}")

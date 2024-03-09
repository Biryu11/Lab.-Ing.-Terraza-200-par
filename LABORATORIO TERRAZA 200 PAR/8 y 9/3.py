# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 20:34:23 2024

@author: Lenovo
"""

def validar_calificacion(calificacion):
    calificacion_numero = float(calificacion)

    assert 0 <= calificacion_numero <= 20, "La calificación debe estar en el rango de 0 a 20"

    print(f"Calificación válida: {calificacion_numero}")

calificacion_ingresada = input("Ingresa la calificación: ")

try:
    validar_calificacion(calificacion_ingresada)
except AssertionError as e:
    print(f"Error: {e}")
except ValueError:
    print("Error: Ingresa un número para la calificación.")

# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 20:36:01 2024

@author: Lenovo
"""

def verificar_lista_no_vacia(lista):
    assert len(lista) > 0, "La lista está vacía"

mi_lista = [1, 2, 3]
verificar_lista_no_vacia(mi_lista)
print("La lista no está vacía.")

otra_lista = []
try:
    verificar_lista_no_vacia(otra_lista)
except AssertionError as e:
    print(f"Error: {e}")

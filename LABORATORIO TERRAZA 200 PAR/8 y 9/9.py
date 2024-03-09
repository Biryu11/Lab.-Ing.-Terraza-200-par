# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 20:40:31 2024

@author: Lenovo
"""

def asegurar_modulo_insertado(nombre_modulo):
    modulo_importado = __import__(nombre_modulo)
    assert modulo_importado is not None, f"No se pudo importar el módulo: {nombre_modulo}"

    print(f"El módulo {nombre_modulo} se ha insertado correctamente.")

asegurar_modulo_insertado("random")

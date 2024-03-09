# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 20:15:13 2024

@author: Lenovo
"""

def verificar_tipo_de_dato(variable, tipo_esperado):
    assert isinstance(variable, tipo_esperado), f"La variable no es del tipo {tipo_esperado}"


#Ejemplo
numero = 1
print(verificar_tipo_de_dato(numero, int))
#La variable no es del tipo <class 'float'>


#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de un modulo
"""
from math import pow

lista = [] #Creando lista vacia
sumatoria = 0 #incializamos variable sumatoria 
desviacion = 0 #inicializamos variable desviacion 

for x in range(0, 7):
    elementos = int(input("Ingrese un valor: "))
    sumatoria += elementos #realizando sumatoria
    lista.append(elementos) #añadiendo elementos a la lista

media = sumatoria/7 #calculando media

for y in range(0, 7):
    desviacion += pow(y - media, 2) 

varianza = desviacion/7

print(varianza)


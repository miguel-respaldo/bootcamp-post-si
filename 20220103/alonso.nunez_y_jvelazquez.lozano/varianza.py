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
tam = int(input('Ingrese el numero de elementos de la varianza: ')) #Tamaño de la lista

for x in range(0, tam):
    elementos = int(input(f"Ingrese valor {x + 1}: ")) #Uso un fstring para enumerar el elemento agregado a la lista
    sumatoria += elementos #realizando sumatoria
    lista.append(elementos) #añadiendo elementos a la lista

media = sumatoria / tam #calculando media

for y in range(0, tam):
    desviacion += pow(lista[y] - media, 2) #Calculo de la desviación

varianza = desviacion / tam

print(f"La varianza es de: {varianza}")


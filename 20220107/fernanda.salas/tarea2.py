#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Multiplicacion de matrices
"""
import numpy

#pedimos el numero de filas y columnas para ambas matrices
matriz1_filas = int(input("Ingrese el numero de filas para la primera matriz: "))
matriz1_columnas = int(input("Ingrese el numero de columnas para la primera matriz: "))

#generamos e imprimimos nuestra matriz con numeros aleatorios
matriz1 = numpy.random.randint(1,100, size=(matriz1_filas, matriz1_columnas))
print(matriz1)

matriz2_filas = int(input("Ingrese el numero de filas para la segunda matriz: "))
matriz2_columnas = int(input("Ingrese el numero de columnas para la segunda matriz: "))

matriz2 = numpy.random.randint(1,100, size=(matriz2_filas, matriz2_columnas))
print(matriz2)

#verificamos si se puede realizar la multiplicacion
if matriz1_columnas != matriz2_filas:
    print("La multiplicacion no se puede realizar")

#inicializamos en 0 la matriz del resultado de la multiplicacion
matriz_res = numpy.zeros((matriz1_filas, matriz2_columnas))

#operaciones para la multiplicacion
for filas in range(0,matriz1_filas):
    for columnas in range(0, matriz2_columnas):
        for mul in range(0,matriz2_filas):
            matriz_res[filas,columnas]+=matriz1[filas,mul] * matriz2[mul,columnas] 

print("El resultado de la multiplicacion es: ")
print(matriz_res)

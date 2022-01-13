#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

lista = list()

for x in range(3):
    lista.append(0)

matriz = list()

for x in range(3):
    matriz.append(lista)

# Imprimir la matriz resultante
for fila in range(3):
    print("[", end=" ")
    for columna in range(3):
        print("{:3d} ".format(matriz[fila][columna]), end="")
    print("]")

matriz[0][0] = 1
matriz[1][1] = 2
matriz[2][2] = 3

# Imprimir la matriz resultante
for fila in range(3):
    print("[", end=" ")
    for columna in range(3):
        print("{:3d} ".format(matriz[fila][columna]), end="")
    print("]")

lista[0] = -1
lista[1] = -2
lista[2] = -3

# Imprimir la matriz resultante
for fila in range(3):
    print("[", end=" ")
    for columna in range(3):
        print("{:3d} ".format(matriz[fila][columna]), end="")
    print("]")




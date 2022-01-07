#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de un modulo
"""
n = int(input("Ingresa el tamano de la matriz n*n: "))
numero = 0

matriz = []

for i in range(n): # 1
    matriz.append([])
    for j in range(n):
        numero += 1
        matriz[i].append(numero)

for i in range(len(matriz)):
    print("[ ", end="")
    for j in range(len(matriz[i])):
        print("\t",matriz[i][j],end="\t")
    print("]")


#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

#matriz = [[1,2],[3,4]]
matriz = []
#matriz = list()

contador = 1

for i in range(2): # 1
    matriz.append([])
    for j in range(2):
        #numero = eval(input("Ingresa un número para la posición de la matriz: "))
        #matriz[i].append(numero)
        matriz[i].append(contador)
        contador += 1

#print(matriz[0][0]) # 1
#print(matriz[0][1]) # 2
#print(matriz[1][0]) # 3
#print(matriz[1][1]) # 4

for i in range(len(matriz)):
    print("[ ", end="")
    for j in range(len(matriz[i])):
        print(matriz[i][j], end=" ")
    print("]")


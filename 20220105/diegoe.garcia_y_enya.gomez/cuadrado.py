#matriz = [[1,2],[3,4]]

#matriz = list(
m = int(input("Ingrese el tamaño deseado para su matriz: "))

#matriz con 0
arr = [[0 for i in range(m)] for j in range (m)]
nivel = 0
val = 0
while val < m * m:
    num = m - (nivel * 2) - 1
    valq = val


for i in range(matriz): # 1
    matriz.append([matriz])
    for j in range(matriz):
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

#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de un modulo
"""


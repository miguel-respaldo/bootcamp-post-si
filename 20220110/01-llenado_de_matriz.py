#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

import random

# matriz de nxm
n = 3
m = 2

# Generación de la matriz con ceros de forma comprimida
matriz = [[random.randrange(1,100) for columna in range(m)] for fila in range(n)]

# [ [ 2  4 ], [ 4  2 ], [ 2  1 ]]

matriz.append(8)
matriz.append("hola")
matriz.append(list())
matriz.append([ 2 , 3, "bu"])
matriz.insert(4,100)
matriz.insert(5,[1,2,3])
matriz.insert(0,[0,0,0])

# Imprimir la matriz resultante
for fila in range(n):
    print("[", end=" ")
    for columna in range(m):
        print("{:3d} ".format(matriz[fila][columna]), end="")
    print("]")

print(matriz)


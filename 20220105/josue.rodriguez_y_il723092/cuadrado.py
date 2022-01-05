#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

n = int(input("Ingresa tamaño del cuadrado: "))

matriz= []
cont = 1

for i in range(n):
    matriz.append([])
    for j in range(n):
        matriz[i].append(0)

for i in range(n**2):
    if matriz[0][i%n]==0:
        matriz[0][i%n]=i+1
    elif matriz[(i+1)%n][-1]==i+1:
        matriz[(i+1)%n][-1]=i
    elif matriz[-1][n-1-i%n]:
        pass

#print(matriz)
for i in range(n):
    print(matriz[i])

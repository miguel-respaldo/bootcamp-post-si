#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later



n = int(input("Ingrese el tam de matriz: "))

k=1


matriz = []
for x in range(n):
    matriz.append([])
    for y in range(n):
        matriz[x].append(0)

lim = n//2
for i in range(lim):
 
    j = i
    while j < n-i-1:
        matriz[i][j] = k
        k += 1
        j+=1
        

    j = i
    while j < n-i-1:
        matriz[j][n-i-1] = k
        k += 1
        j+=1
    
    j = n-i-1
    while j > i:
        matriz[n-i-1][j] = k
        k+=1
        j-=1

    j= n-i-1
    while j > i:
        matriz[j][i] = k
        k+=1
        j-=1

if n%2 == 1:
    i = int((n+1)/2) - 1
    matriz[i][i] = n*n


for x in range(n):
    print("[",end="\t")
    for y in range(n):
        print(matriz[x][y],end="\t")
    print("]")

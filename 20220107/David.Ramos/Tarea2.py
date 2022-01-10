#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

import random

print("Programa para multiplicar matrices matriz A por matriz B")

while True:
    filas1 = int(input("Ingresa el numero de filas de la matriz A: "))
    columnas1 = int(input("Ingresa el numero de columnas de la matriz A: "))
    filas2 = int(input("Ingresa el numero de filas de la matriz B: "))
    columnas2 = int(input("Ingresa el numero de columnas de la matriz B: "))

    if columnas1 == filas2:
        break
    
    if input("El numero de columnas de la matriz A debe ser igual al numero de filas que de la matriz B. Volver a intentar? s/n: ") == "n" : quit() 
    
A = []

for i in range(filas1) : 
    A.append([])
    for j in range(columnas1) : A[i].append(random.randrange(0,99))
    
print("La matriz A queda asi:")
for x in range(filas1):
    print("[",end="\t")
    for y in range(columnas1):
        print(A[x][y],end="\t")
    print("]")

B = []

for i in range(filas2) : 
    B.append([])
    for j in range(columnas2) : B[i].append(random.randrange(0,99))
    
print("La matriz B queda asi:")
for x in range(filas2):
    print("[",end="\t")
    for y in range(columnas2):
        print(B[x][y],end="\t")
    print("]")
    
C = []

newValue = 0
for i in range(filas1) : 
    C.append([])
    for j in range(columnas2) : 
        for k in range(columnas1) : 
            newValue += A[i][k] * B[k][j]
        C[i].append(newValue)
        newValue = 0
    
print("La matriz resultante es:")

for x in range(filas1):
    print("[",end="\t")
    for y in range(columnas2):
        print(C[x][y],end="\t")
    print("]")

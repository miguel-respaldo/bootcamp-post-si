#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

import random

matrizProducto=list()     #Matriz resultante

print("Programa para calcular el producto de matrices.\n")

fila_m1=int(input("Ingresa el tamano de la fila de la primer matriz\n"))
col_m1=int(input("Ingresa el tamano de la columna de la primer matriz\n"))
fila_m2=int(input("Ingresa el tamano de la fila de la segunda matriz\n"))
col_m2=int(input("Ingresa el tamano de la columna de la segunda matriz\n"))

if col_m1 == fila_m2:  # Comprueba si se puede realizar este producto
#2x3 y 3x2 se puede = 2x[3] [3]x2 = al ser el mismo se puede, caso contrario no.
#2x3 y 2x3 no se puede

    matrizA=list() #se crea matrizA
    matrizB=list() #se crea matrizB

    for i in range(fila_m2):
        matrizProducto.append([])
        for j in range(col_m2):
            matrizProducto[i].append(0)

    for i in range(fila_m1): #se llena la matriz con numeros aleatorios tope a 100
        matrizA.append([])
        for j in range(col_m1):
            matrizA[i].append(random.randrange(100))

    print("\n\t  Matriz A: \n") #se imprime la matriz A
    for x in range(fila_m1):
            print('\t[',end='  ')
            for y in range(col_m1):
                print(matrizA[x][y],end='  ')
            print(']')

    for i in range(fila_m2): #Se empieza a llenar la matriz B
        matrizB.append([])
        for j in range(col_m2):
                    matrizB[i].append(random.randrange(100))

    print("\n\t  Matriz B: \n") #se imprime la matriz B
    for y in range(fila_m2):
            print('\t[',end='  ')
            for z in range(col_m2):
                print(matrizB[y][z],end='  ')
            print(']')

    for k in range(col_m2):   #se obitenen columnas de la matriz resultante
        for i in range(fila_m1): 
            suma = 0    
            for j in range(col_m1):     
                suma += matrizA[i][j]*matrizB[j][k] #suma de ambos elementos A y B
                matrizProducto[i][k] = suma # se guarda el valor en la posición de [i][k]

    print("\n\t Matriz resultante: \n")
    for i in range(fila_m2): 
            print('\t[', end='  ')
            for j in range(col_m2):
                print(matrizProducto[i][j], end='  ') 
            print(']')
else:    
    print('Esta multiplicacion de matrices no puede realizarse\n')

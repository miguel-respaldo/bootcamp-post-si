#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Tarea 2./ multiplicacion de matrices 
"""

def main():
    """
    Comentario de la función
    """
#Extraer libreria de random para generar el llenado de las matrices
import random

producto=list()     #Matriz resultante

print("Bienvenido, Programa que ejecuta el producto de matrices.\n")
fila_matriz1=int(input("Introduzca el tamanno de la fila de la matriz 1\n"))
columna_matriz1=int(input("Introduzca el tamanno de la columna de la matriz 1\n"))
fila_matriz2=int(input("Introduzca el tamanno de la fila de la matriz 2\n"))
columna_matriz2=int(input("Introduzca el tamanno de la columna de la matriz 2\n"))

# Verificar si la operacion es valida
if columna_matriz1 == fila_matriz2: 
#Se crean las matriz del orden que declara el usuario

    matrizA=list()
    matrizB=list()

#Se crea el espacio vacio del producto matricial

    for i in range(fila_matriz2):
        producto.append([])
        for j in range(columna_matriz2):
            producto[i].append(0)

#########'Matriz A creacion y llenado'##############
#Llenar matriz A con numero random de 0 y 100

    for i in range(fila_matriz1):
        matrizA.append([])
        for j in range(columna_matriz1):
            matrizA[i].append(random.randrange(0,100,1))

#despliegue de matriz generada

    print("\tPrimera Matriz generada\n")
    for x in range(fila_matriz1):
            print('[',end='\t')
            for y in range(columna_matriz1):
                print(matrizA[x][y],end='\t')
            print(']')
####################################################
#llenado de matriz B 
    for i in range(fila_matriz2):
        matrizB.append([])
        for j in range(columna_matriz2):
                    matrizB[i].append(random.randrange(0,100,1))

#despliegue de matriz generada

    print("\tSegunda Matriz generada")
    for x in range(fila_matriz2):
            print('[',end='\t')
            for y in range(columna_matriz2):
                print(matrizB[x][y],end='\t')
            print(']')
###################################################
#####Matriz resultante #########

    for c in range(columna_matriz2):   #para obtener las columnas de la  resultante'
        for i in range(fila_matriz1):
            suma = 0    #guardar suma de los dos elementos
            for j in range(columna_matriz1):    #donde se haran las operacion fila columna 
                suma += matrizA[i][j]*matrizB[j][c]
                producto[i][c] = suma

    print("\t Resultado del producto de la matriz\n")
    for i in range(fila_matriz2): 
            print('[', end='\t')
            for j in range(columna_matriz2):
                print(producto[i][j], end='\t')
            print(']')
###################################################
###'Caso contrario de que no se pueda haceer el producto'

else:    
    print('No se puede realizar el producto de matrices\n')


if __name__ == "__main__":
    main()


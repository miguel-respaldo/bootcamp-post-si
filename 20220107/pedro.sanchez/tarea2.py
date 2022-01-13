#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""

Ejercicio para la multiplicaión de dos matrices

"""

import random

#variables globales
tamanio=[0,0,0]
mat1=[]
mat2=[]
mat3=[]

def ranOpt():
    for filas in range(tamanio[0]):
        mat1.append([])
        for columnas in range(tamanio[1]):
            mat1[filas].append(random.randrange(0, 1000))

    for filas in range(tamanio[1]):
        mat2.append([])
        for columnas in range(tamanio[2]):
            mat2[filas].append(random.randrange(0, 1000))

def ingresar():
    print('Ingresa los valores de la primer matriz')
    for filas in range(tamanio[0]):
        mat1.append([])
        for columnas in range(tamanio[1]):
            val=int(input('Mat1[{}][{}]: '.format(filas, columnas)))
            mat1[filas].append(val)

    print('Ingresa los valores de la segunda matriz')
    for filas in range(tamanio[1]):
        mat2.append([])
        for columnas in range(tamanio[2]):
            val=int(input('Mat2[{}][{}]: '.format(filas, columnas)))
            mat2[filas].append(val)

def multiplicar():
    for filas in range(tamanio[0]):
        mat3.append([])
        for columnas in range(tamanio[2]):
            mat3[filas].append(0)
            for i in range(tamanio[1]):
                mat3[filas][columnas]=mat3[filas][columnas] + mat1[filas][i]*mat2[i][columnas]
                
            print('Mat3[{}][{}]={}'.format(filas, columnas, mat3[filas][columnas]))


def main():

    print('Ingresa 1 para una multiplicación random')
    op = input('y 2 para ingresar los valores: ')
    print(int(op))

    if op=='1':
        print('Ingresa los tamaños de las matrices Mat1[m][n] y Mat2[n][p]')
        tamanio[0]=int(input('m: '))
        tamanio[1]=int(input('n: '))
        tamanio[2]=int(input('p: '))
        ranOpt()

    elif op=='2':
        print('Ingresa los tamaños de las matrices Mat1[m][n] y Mat2[n][p]')
        tamanio[0]=int(input('m: '))
        tamanio[1]=int(input('n: '))
        tamanio[2]=int(input('p: '))
        ingresar()

    multiplicar()
  


if __name__ == "__main__":
    main()


#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
import random

lin_matriz1 = int(input('Filas de la primera matriz: '))
col_matriz1 = int(input('Columnas de la primera matriz: '))
print('')
lin_matriz2 = int(input('Filas de la segunda matriz: '))
col_matriz2 = int(input('Columnas de la segunda  matriz: '))

#generar matriz numero 1
matriz1 = [[random.randint(0,9) for m in range(col_matriz1)] for n in range(lin_matriz1)]

#generar matriz numero 2
matriz2 = [[random.randint(0,9) for m in range(col_matriz2)] for n in range(lin_matriz2)]


print('')
if col_matriz1 == lin_matriz2:
    #Imprimimos la matriz 1
    print('Matriz 1')
    for fila in range(lin_matriz1): 
        print('[', end=' ')
        for columna in range(col_matriz1): 
            print('{:3d} '.format(matriz1[fila][columna]), end='')
        print(']')

    print('')
    #Imprimimos la matriz 2
    print('Matriz 2')
    for fila2 in range(lin_matriz2): 
        print('[', end=' ')
        for columna2 in range(col_matriz2): 
            print('{:3d} '.format(matriz2[fila2][columna2]), end='')
        print(']')

    print('')
    #Calculo de la matriz resultante 
    print('Matriz resultante')
    matriz3 = [[sum(a * b for a, b in zip(lin_matriz1, col_matriz2))
                              for col_matriz2 in zip(*matriz2)]
                                    for lin_matriz1 in matriz1]
    
    for r in matriz3: #Impresion de matriz resultante
        print(r)
else:
    print('Operacion imposible de realizar, intentelo de nuevo')


#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

import random

def matrix_size(n):
    rows=int(input("Número de filas en matriz {}: ".format(n)))     #Se solicita número de filas
    cols=int(input("Número de columnas en matriz {}: ".format(n)))  #Se solicita número de columnas
    return rows, cols               #Se regresan los valores de fila y columna

def fill_matrix(rows,cols):
    matrix = []                     #Se crea matriz vacía
    for i in range(rows):           #Se itera el número de filas
        matrix.append([])           #Se crea la matiz de la nueva fila vacía
        for j in range(cols):       #Se itera el número de columnas
            matrix[i].append(random.randrange(10)) #Se agrega un valor aleatorio a la posición indicada
    return matrix

def matrix_mult(m1,m2):
    ans=[]
    for i in range(len(m1)):
        ans.append([])
        for k  in range(len(m2[i])):
            x=0
            for j in range(len(m2)):
               x+=m1[i][j]*m2[j][k]
            ans[i].append(x)
    return ans

def print_matrix(matrix):
    for rows in matrix:
        row = "[\t"
        for col in rows:
            row += str(col) + "\t"
        print(row+"]")


while True:
    rows_m1, cols_m1=matrix_size(1)
    rows_m2, cols_m2=matrix_size(2)
    
    if cols_m1 == rows_m2:
        break
    else:
        print("Matrices no válidas para su multiplicación, intente de nuevo.")

m1=fill_matrix(rows_m1,cols_m1)
m2=fill_matrix(rows_m2,cols_m2)
m3=matrix_mult(m1,m2)
print("Matriz 1:")
print_matrix(m1)
print("Matriz 2:")
print_matrix(m2)
print("Resultado de su multiplicación:")
print_matrix(m3)








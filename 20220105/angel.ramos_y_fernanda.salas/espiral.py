#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

#matriz = [[1,2],[3,4]]
matriz = []
#matriz = list()
n = eval(input("ingrese tamaño matriz: "))


#crear matriz de n X n de ceros

for i in range(n):
    matriz.append([])
    for j in range(n): 
        matriz[i].append(0)

contador = 0
m=n
# posiciones
a=0 
b=n-1
c=n-1
e=n-1

while contador!=n**2: #hasta que el contador llegue a n al cuadrado

#de izq a derecha
    for i in range(m):
        contador = contador + 1
        matriz[a][i+a] = contador
    m=m-1
    a=a+1

#de arriba hacia abajo
    for i in range(m):
        contador = contador + 1
        matriz[a+i][b] = contador
    b=b-1

#de derecha a izq
    for i in range(m):
        contador = contador + 1
        matriz[c][b-i] = contador
    m=m-1
    c=c-1

#de abajo hacia arriba
    for i in range(m):
        contador = contador + 1
        matriz[c-i][a-1] = contador 

#impresión de la matriz
for i in range(len(matriz)):
    print("[ ", end="")
    for j in range(len(matriz[i])):
        print(matriz[i][j], end=" ")
    print("]")




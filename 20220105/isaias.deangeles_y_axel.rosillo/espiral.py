#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Practica: Matriz espiral
"""

def main():
    n = int (input ( "Ingrese la dimension de la matriz: " ) )
    
    matriz = [[0 for i in range(n)] for j in range(n)]
    nivel = 0
    coordenada = 0

    while coordenada < n * n:
        
        num = n - (nivel * 2) - 1
        temp = coordenada

        for i in range(num):
            temp += 1
            matriz[nivel][i+nivel] = temp
            matriz[nivel+i][n-nivel-1] = temp + num
            matriz[n-nivel-1][n-nivel-i-1] = temp + num * 2
            matriz[n-nivel-i-1][nivel] = temp + num * 3
         
        nivel += 1
        coordenada += num * 4

    for i in matriz:
        for j in i:
            print('%3s' % j, end='')
        print("")


if __name__ == "__main__":
    main()


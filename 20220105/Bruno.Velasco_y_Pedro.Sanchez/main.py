#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Matriz espiral
"""

def main():
    """
    main
    """
    
    n=15
    #n = eval(input("Ingrese n para la matriz: "))
    

    matriz = []

    for i in range(n):
        matriz.append([])
        for j in range(n):
            matriz[i].append(0)
    
    contador = 1
    x, y =0, 0

    # matriz[columna][fila]
    s = False
    max = 0
    for i in range(n):
        for j in range(n):
            matriz[j][i] = contador
            contador += 1
    #imprimir(matriz)

    contador = 1
    for i in range(n):
        max += len(matriz[i])
    print (max)
    for i in range(int(n)):
        
        # Primer fila
        for a in range(0+i, n-1-i):
            matriz[0+i][a] = contador
            contador+=1
            if contador > max: break
        if contador > max: break
        # Ultima columna
        for a in range(0+i, n-1-i):
            matriz[a][n-1-i] = contador
            contador+=1
            if contador > max: break
        if contador > max: break
        # Ultima fila
        for a in range(n-1-i,0,-1):
            matriz[n-1-i][a] = contador
            contador+=1
            if contador > max: break
        if contador > max: break
        # Primer columna
        for a in range(n-1-i,0+i,-1):
            matriz[a][0+i] = contador
            contador+=1
            if contador > max: break
        if contador > max: break

        
    imprimir(matriz)
      
def imprimir(matriz):
    # imprimir la matriz
    for i in range(len(matriz)):
        print("[ ", end="")
        for j in range(len(matriz[i])):
            if matriz[i][j] >= 10:
                print(matriz[i][j], " ", end=" ")
            elif matriz[i][j] >= 100:
                    print(matriz[i][j])
            else:
                print(matriz[i][j], "  ", end=" ")
        print("]")




if __name__ == "__main__":
    main()

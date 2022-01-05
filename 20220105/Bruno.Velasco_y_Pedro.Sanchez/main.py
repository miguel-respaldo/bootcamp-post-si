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
    

    #n = eval(input("Ingrese n para la matriz: "))
    n=6

    matriz = []

    for i in range(n):
        matriz.append([])
        for j in range(n):
            matriz[i].append(0)
    
    contador = 1
    for a in range(n):
        # Primer fila
        for b in range(n):
            matriz[a][b] = contador
            contador+=1
        
        #for c in range():
        #    matriz[][] = contador
        #    contador+=1

        
    

    for i in range(len(matriz)):
        print("[ ", end="")
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print("]")





if __name__ == "__main__":
    main()


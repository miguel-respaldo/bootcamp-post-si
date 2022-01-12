#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Tarea: Multiplicacion de matrices
"""
import numpy as np

def main():
   

    n_A = int(input("Ingrese el numero de filas de la matriz A: \n"))
    m_A = int(input("Ingrese el numero de columnas de la matriz A: \n"))

    matrizA = np.random.randint(0, 100, size=(n_A, m_A)) #Llena matriz con random
    print(matrizA)
    
    n_B = int(input("\n\nIngrese el numero de filas de la matriz B: \n"))
    m_B = int(input("Ingrese el numero de columnas de la matriz B: \n"))

    matrizB = np.random.randint(0, 100, size=(n_B, m_B)) #Llena matriz B con random
    print(matrizB)
    
    
    if m_A == n_B:
        print("\n\nEl resultado de A * B es:")
        result = []
        for i in range(len(matrizB[0])): #Ciclo para calcular la matriz resultante
            total = 0
            for j in range(len(matrizA)): 
                total += matrizA[j] * matrizB[j][i]
            result.append(total)
            
            
        for i in result: #Ciclo para imprimir
            print("[", end="")
            for j in i:
                print('%3s' % j, end=' ')
            print("]")
    else:
        print("\n\nNo se pueden multiplicar :(")


if __name__ == "__main__":
    main()

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

    matrizA = np.random.randint(0, 100, size=(n_A, m_A))
    print(matrizA)
    
    n_B = int(input("\n\nIngrese el numero de filas de la matriz B: \n"))
    m_B = int(input("Ingrese el numero de columnas de la matriz B: \n"))

    matrizB = np.random.randint(0, 100, size=(n_B, m_B))
    print(matrizB)
    
    if m_A == n_B:
        print("\n\nEl resultado de A * B es:")
        print(matrizA.dot(matrizB))
    else:
        print("\n\nNo se pueden multiplicar :(")


if __name__ == "__main__":
    main()

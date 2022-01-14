#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

import random

# Genera matriz random
matriz = [random.randint(1,100) for x in range(10000)]
#print(matriz)
matriz.sort()              # Ordenamiento con funcion sort

def bubbleSort(matriz): # Ordenamiento con metodo burbuja
    n = len(matriz)
 
    # Se recorren todos los elementos
    for i in range(n-1):
        
        # Se recorren los elementos de dos en dos con el elemnto siguiente
        for j in range(0, n-i-1):
 
            # Realiza un cambio si el elemento siguiente es mayor
            if matriz[j] > matriz[j + 1] :
                matriz[j], matriz[j + 1] = matriz[j + 1], matriz[j]

bubbleSort(matriz)
 
print ("La matriz arreglado: ")
for i in range(len(matriz)):
    print (matriz[i],end=" ")

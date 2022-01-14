#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Burbuja
"""
import time

print("Programa para ordenamiento Burbuja")
tam = int(input ('Ingresa el numero de elementos del array ')) 

array = []

for i in range(0,tam):
    array.append(input('Ingresa el elemento a almacenar en el arreglo\n'))

timestart = time.time() #funcion para el tiempo
print ('Primer array', array)

for i in range(tam-1):
    for j in range (tam-1):
            if array[j] > array[j+1]: #si el valor del array en esa posicion es mayor que la sig posicion, cambia
                aux = array[j]  # aux que guarda el valor elemento actual
                array[j] = array[j+1] # se guarda el valor de la sig posición 
                array[j+1] = aux # la sig posicion guarda ahora el valor de aux
                print(array[j])
print('Segundo array (ordenado)', array)
print('Este es el tiempo final')
print(time.time() - timestart)

#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

from random import randint
import time

arreglo = [ x for x in range(randint(10,1200))] # lista de N elementos random con comprehesion

# llenando lista de N elmentos de numeros random
for x in arreglo:
    arreglo[x] = randint(10,50)

arregloSort = arreglo #copia del arreglo para el sort de python

start = time.time()
arregloSort.sort()
end= time.time()
print(f"Tiempo que le toma al Sort de python con: {len(arreglo)} elementos: | {end-start} ")


isDesordenado = True
start = time.time()
while isDesordenado: #mientras siga desordenado se va a repetir
    isDesordenado = False # levantamos bandera que se mantiene si no se realiza ningun swap
    for i in range(len(arreglo)-1):#-1 porque al llegar al ultimo elemento compararia con None
        if arreglo[i] > arreglo[i+1]: #esta desordenado y hacemos swap
            temp=arreglo[i] # temporal para guardar el valor actual
            arreglo[i] = arreglo[i+1] #swap derecha a izquierda
            arreglo[i+1] = temp #swap izquierda a derecha
            isDesordenado = True # si entro al if, es porque aun existia un elemento desordenado
end = time.time()

print(f"Tiempo que le toma a burbuja con: {len(arreglo)} elementos: | {end - start} ")

if len(arregloSort) == len(arreglo):
    print(arregloSort == arreglo)
    print("FIN")

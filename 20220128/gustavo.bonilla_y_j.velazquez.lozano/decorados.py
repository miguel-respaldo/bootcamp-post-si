#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
from operator import le
from random import randint
import time

arreglo1 = [ x for x in range(randint(1000,1200))] # lista de N elementos random con comprehesion
 # llenando lista de N elmentos de numeros random
for x in arreglo1:
    arreglo1[x] = randint(10,50)

arreglo2 = arreglo1

def log(bravo):
    def wrapper(*args,**kwargs):
        start = time.time()
        
        print(f"Inicia funcion con {len(args[0])} elementos {time.time() -start} ",end="")
        ordenado = bravo(*args,**kwargs)
        with open("log.txt","a") as f:
            f.write("Inicia funcion con ")
            f.write(str(len(args[0])))
            f.write(" elementos "),
            f.write(str(time.time() -start))
            f.write(" y tardo ")
            f.write(str(time.time()-start))
            f.write("\n")
          
        end = time.time()
        print(f" y tardo {end-start} |")
        return(ordenado)  

    return wrapper

@log
def sort_list(arreglo):
    print("con Sort")
    arreglo.sort()
    return arreglo

@log
def bubblesort(arreglo):
    print("con Bubble Sort")
    isDesordenado = True
    while isDesordenado: #mientras siga desordenado se va a repetir
        isDesordenado = False # levantamos bandera que se mantiene si no se realiza ningun swap
        for i in range(len(arreglo)-1):#-1 porque al llegar al ultimo elemento compararia con None
            if arreglo[i] > arreglo[i+1]: #esta desordenado y hacemos swap
                temp=arreglo[i] # temporal para guardar el valor actual
                arreglo[i] = arreglo[i+1] #swap derecha a izquierda
                arreglo[i+1] = temp #swap izquierda a derecha
                isDesordenado = True # si entro al if, es porque aun existia un elemento desordenado
    return arreglo

with open("log.txt","w+") as f:
    f.write("Ordenamientos\n")

resultado_bubble = bubblesort(arreglo1) 
resultado_sort =  sort_list(arreglo2)



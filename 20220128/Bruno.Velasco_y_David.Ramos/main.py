#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
import datetime
import time
import random

f = open("log.txt","w")

def log(funcion):
    def wrapper(args):
        
        
        f.write("La función con argumentos: \n" + funcion(args) + " fue llamada  a las " + str(datetime.datetime.now()) + "\n")
        
        #res = funcion(*args, **kwargs)
        #return res"
        
    return wrapper

@log
def burbuja(cantidad):
    
    sutano = cantidad

    lista = [random.randint(0,999) for x in range(sutano)]

    timestart = time.time()
    variable = "lista desordenada es esta: \n"
    #print (lista)
    variable +=  str(lista) + "\n"

    for i in range(sutano-1):
        for o in range(sutano-1):
            if lista[o] > lista[o+1]:
                fulano = lista[o]
                lista[o] = lista[o+1]
                lista[o+1] = fulano
            
    variable += 'Esta es la lista ordenadita \n'
    variable += str(lista) + '\n'
    variable += 'Este tiempo dure paps: \n'
    variable +=  str(time.time() - timestart) + '\n\n'

    return variable

@log
def ordenamientoSort(cantidad):
    sutano = cantidad

    lista = [random.randint(0,999) for x in range(sutano)]

    timestart = time.time()
    variable = 'lista desordenada es esta: \n'
    variable += str(lista) + '\n'

    lista.sort()
            
    variable += 'Esta es la lista ordenadita\n'
    variable += str(lista) +'\n'
    variable += 'Este tiempo dure paps: '
    variable += str(time.time() - timestart) +'\n'
    
    return variable

print("Que tipo de ordenamiento deseas")
print("1) Burbuja")
print("2) Sort")
seleccion1 = int(input())

seleccion2 = int(input("Cuantos numeros se van a generar? "))

if (seleccion1 == 1):
    burbuja(seleccion2)
elif (seleccion1 == 2):
    ordenamientoSort(seleccion2)
else:
    print("Invalido")

f.close()
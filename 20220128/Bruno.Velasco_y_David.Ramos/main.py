#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
import datetime
from statistics import variance
import time
import random

def log(funcion):

    f = open("log.txt","a")
    f.write("La función con argumentos: \n" + funcion() + " fue llamada  a las " + str(datetime.datetime.now()) + "\n")
    f.close()
    #res = funcion(*args, **kwargs)
    #return res"

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
    variable +=  str(time.time() - timestart) + '\n'

    return variable

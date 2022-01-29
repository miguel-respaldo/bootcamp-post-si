#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de un modulo
"""

import datetime
import time
import random

def timer(funcion):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        funcion(*args, **kwargs)
        fin = time.time()
        return fin - inicio

    return wrapper

###############loguer#######################

def log(funcion):
    def wrapper(*args, **kwargs):

        time= funcion(*args, **kwargs)
        f = open("log.txt","a")
        f.write("La función burbuja con argumentos: " + " ".join([str(arg) for arg in args]) + " fue llamada  a las " + str(datetime.datetime.now()) + "\n" + "y tardó en ejecutarse: " + str(time) + " segundos"+"\n")
        #f.write("La función sort tardó en ejecutarse:segundos")
        f.close()
        res = funcion(*args, **kwargs)
        return res, time

    return wrapper

#############ORDENAMIENTO con BURBUJA ##################

@timer
def burbuja(tam):
    lista = [random.randint(0,999) for x in range(tam)]
    for i in range(tam-1):
      for o in range(tam-1):
          if lista[o] > lista[o+1]:
              elemento = lista[o]
              lista[o] = lista[o+1]
              lista[o+1] = elemento
    lista_ordenada=lista

@log
def exe_bur(tam):   
    return burbuja(tam)

exe_bur(1000)
#print(tiempo)
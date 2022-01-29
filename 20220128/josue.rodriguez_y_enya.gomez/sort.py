#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
# SPDX-License-Identifier: GPL-3.0-or-later

#timer

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
        f.write("La función sort con argumentos: " + " ".join([str(arg) for arg in args]) + " fue llamada  a las " + str(datetime.datetime.now()) + "\n" + "y tardó en ejecutarse: " + str(time) + " segundos"+"\n")
        #f.write("La función sort tardó en ejecutarse:segundos")
        f.close()
        res = funcion(*args, **kwargs)
        return res, time

    return wrapper

#############ORDENAMIENTO con SORT ##################
@timer
def funcion_sort(tam):
     lista = [random.randint(0,999) for x in range(tam)]
     lista.sort()

@log
def exe(tam):
     return funcion_sort(tam)

exe(1000)
#print("Se tardo", tiempo, "segundos")

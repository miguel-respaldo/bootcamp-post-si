#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de un modulo
"""
import random
import datetime
import time

def log(funcion):
    def wrapper(*args):
        f = open("log.txt","a")
        f.write("La función con argumentos: " + " ".join([str(arg) for arg in args]) + " fue llamada  a las " + str(datetime.datetime.now()) + "\n")
        f.close()
        funcion(*args)
       # return res

    return wrapper

@log
def burbuja(ordenar):   # Funcion de ordenamiento burbuja
    for i in range(1,len(ordenar)): # Ciclo de 1 a la longitud de la lista
        for j in range(0,len(ordenar)-i):
            if(ordenar[j+1] < ordenar[j]): # Compara si el siguiente elemento es menor
                aux=ordenar[j];
                ordenar[j]=ordenar[j+1];
                ordenar[j+1]=aux; # Hace el intercambio
    print (ordenar)

@log
def resta(a,b):
    return a-b

lista = random.sample(range(0, 1000), 1000) # Crea una lista de numeros aleatorios
burbuja(lista)

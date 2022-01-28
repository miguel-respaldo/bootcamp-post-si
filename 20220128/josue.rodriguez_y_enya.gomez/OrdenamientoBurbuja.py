#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

import random
import time
print ('Programa para ordenar una lista')
sutano = int(input ('¿cuantos numeros vamos a ordenar? '))

lista = [random.randint(0,999) for x in range(sutano)]

timestart = time.time()
print ('lista desordenada es esta: ')
print (lista)

for i in range(sutano-1):
    for o in range(sutano-1):
        if lista[o] > lista[o+1]:
            fulano = lista[o]
            lista[o] = lista[o+1]
            lista[o+1] = fulano
        
print ('Esta es la lista ordenadita')
print (lista)
print ('Este tiempo dure paps: ')
print(time.time() - timestart)


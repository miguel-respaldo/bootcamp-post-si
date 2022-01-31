#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

import datetime
import time
import random

def log(funcion):
    def wrapper(*args, **kwargs):
    	f = open('log.txt', 'a')
    	f.write('La funcion con argumentos: ' + ''.join([str(arg) for arg in args]) + ' fue llamada a las ' + str(datetime.datetime.now()) + '\n')
    	f.write('')
    	f.close()
    	res = funcion(*args, **kwargs)
    	return res
    
    return wrapper
    
@log
def ordenamiento(orden):
    n = len(orden) #Determinando largo de la lista
    
    for i in range(n):
    	for j in range(0, n - 1):
    		if orden[j] > orden[j + 1]:
    		    orden[j], orden[j + 1] = orden[j + 1], orden[j]
    
    print('lista ordenada: ', orden)

lista = [random.randint(1, 50) for x in range(10)]

ordenamiento(lista)

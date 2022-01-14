#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de ordenamiento burbuja
"""
import time
import random 

def bubbleSort(array):
    n = len(array)

    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

inicio=time.time()
array = [random.randint(1,1000)for x in range(10000)]
bubbleSort(array)
print(array)
fin=time.time()
print("tiempo de ejecución: {:.5} segundos".format(fin-inicio))




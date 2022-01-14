#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

import time
import random

array = [random.randint(1,50) for x in range(10000)]

def bubbleSort(array):
    tam = len(array)

    for i in range(0, tam):
        for j in range(0, tam-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]


beginning = time.time()
bubbleSort(array)
end = time.time()
elapsed_time = round((end-beginning)*1000, 3)

print("\nLista ordenada:\n\n", array)

print("\nTiempo de ejecución del ordenamiento burbuja:", elapsed_time, "milisegundos\n")

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
import time

tiempo_ejecucion = time.time() #Tiempo de ejecución
lista = [random.randint(1, 50) for x in range(10)] #Generando lista random
print('Lista en desorden: ', lista)
n = len(lista) #Determinando largo de lista

for i in range(n):
    for j in range(0, n - 1):
        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]
print('')
print('Lista ordenada:', lista)
print(f'Tiempo de ejecucion total: {time.time() - tiempo_ejecucion} seg.')


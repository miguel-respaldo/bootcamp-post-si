#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo usando sort
"""
import random
import time

inicio=time.time()
lista = [random.randint(1,1000) for x in range(10000)]

lista.sort()
print(lista)
fin=time.time()

print("El tiempo del proceso es: {:.4} segundos".format(fin-inicio))

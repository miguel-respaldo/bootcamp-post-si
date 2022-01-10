#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

import random

n = 3
m = 2

# Generación de la matriz con ceros de forma comprimida
matriz = [[random.randrage(1,100) for columna in range(n)] for fila in range(m)]

# Imprimir la matriz resultante
for fila in range(tamanio):
    print("[", end=" ")
    for columna in range(tamanio):
        print("{:3d} ".format(matriz[fila][columna]), end="")
    print("]")



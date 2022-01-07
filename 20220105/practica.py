#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

# inicializamos la matriz
matriz = list()

# Pedimos el tamaño del cuadrado al usuario
tamanio = int(input("Escribe el tamaño del cuadrado: "))

# Genero una matriz con ceros del tamaño nxn
for i in range(tamanio):
    matriz.append(list())
    for j in range(tamanio):
        matriz[i].append(0)




# Imprimir la matriz resultante
for i in range(tamanio):
    print("[", end=" ")
    for j in range(tamanio):
        print("{:3d} ".format(matriz[i]))
    print("]")

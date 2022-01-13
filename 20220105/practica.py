#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

# inicializamos la matriz
matriz = list()

direccion = "derecha"

# posiciones de la matriz en "x" y "y"
pos_x = 0
pos_y = 0

# Pedimos el tamaño del cuadrado al usuario
tamanio = int(input("Escribe el tamaño del cuadrado: "))

# Limites de la matriz para la dirección
max_x = tamanio
max_y = tamanio
min_x = 1
min_y = 0


# Genero una matriz con ceros del tamaño nxn
for filas in range(tamanio):
    matriz.append(list())
    for columnas in range(tamanio):
        matriz[filas].append(0)

# Generación de la matriz con ceros de forma comprimida
#matriz = [[0 for columnas in range(tamanio)] for filas in range(tamanio)]

# Llenamos la matriz
for contador in range(tamanio*tamanio):

    # Asignamos el valor a la posición
    matriz[pos_x][pos_y] = contador + 1
    #print(f"({pos_x},{pos_y}) = {contador} -> {direccion}")

    # avanzamos en la matriz
    if  direccion == "derecha":
        pos_y += 1
    elif direccion == "abajo":
        pos_x += 1
    elif direccion == "izquierda":
        pos_y -= 1
    elif direccion == "arriba":
        pos_x -= 1

    # cambiamos de dirección
    if pos_y == max_y and direccion == "derecha":
        pos_y -= 1
        pos_x += 1
        max_y -= 1
        direccion = "abajo"

    if pos_x == max_x and direccion == "abajo":
        pos_x -= 1
        pos_y -= 1
        max_x -= 1
        direccion = "izquierda"

    if pos_y == min_y and direccion == "izquierda":
        min_y += 1
        direccion = "arriba"

    if pos_x == min_x and direccion == "arriba":
        min_x += 1
        direccion = "derecha"


# Imprimir la matriz resultante
for fila in range(tamanio):
    print("[", end=" ")
    for columna in range(tamanio):
        print("{:3d} ".format(matriz[fila][columna]), end="")
    print("]")


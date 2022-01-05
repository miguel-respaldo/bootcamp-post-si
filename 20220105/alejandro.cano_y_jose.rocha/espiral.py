#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Práctica: Número al cuadrado en espiral
"""
#Pedimos el valor de la matriz
n = int(input("Ingrese el número del tamaño de la matriz (nxn): ")

#Se genera una matriz nxn
matriz = [[0 for i in range (n)] for j in range (n)]

#Numero de fila
fila = 0

#Posicion
pos = 0

#Aseguramos que no se exceda el número de posiciones de la matriz indicada
while pos < n*n:
    valor = n - (fila*2) -1
    

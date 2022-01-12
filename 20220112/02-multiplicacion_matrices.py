#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

import random

matriz1 = []
matriz2 = []
resultado = []

n1=eval(input("Ingresa el valor de n1: "))
m1=eval(input("Ingresa el valor de m1: "))

n2=eval(input("Ingresa el valor de n2: "))
m2=eval(input("Ingresa el valor de m2: "))

if m1 != n2:
    print("No se puden multiplicar")
    exit(1)

for i in range(n1):
    matriz1.append([])
    for j in range(m1):
        matriz1[i].append(random.randint(1,5))

for i in range(n2):
    matriz2.append([])
    for j in range(m2):
        matriz2[i].append(random.randint(1,5))


print("Matriz 1")
for i in range(n1):
    print("[ ", end="")
    for j in range(m1):
        print(matriz1[i][j], end=" ")
    print("]")

print("Matriz 2")
for i in range(n2):
    print("[ ", end="")
    for j in range(m2):
        print(matriz2[i][j], end=" ")
    print("]")


for i in range(n1):
    resultado.append([])
    for j in range(m2):
        suma = 0
        for k in range(m1):
            suma += matriz1[i][k] * matriz2[k][j]
        resultado[i].append(suma )

print("Resultado")
for i in range(n1):
    print("[ ", end="")
    for j in range(m2):
        print(resultado[i][j], end=" ")
    print("]")


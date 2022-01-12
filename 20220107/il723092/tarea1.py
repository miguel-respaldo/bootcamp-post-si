#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
    Carro -> on/off 1
    Casa -> on/off 2
    Perro -> on/off 4
    Gato -> on/off 8
    Pez -> on/off 16
    Moto -> on/off 32
    Zapato -> on/off 64
    Navidad -> on/off 128
"""

lista = ["Carro","Casa","Perro","Gato","Pez","Moto","Zapato","Navidad"]

multivar=-1

while multivar<0 or multivar > 255:     #Se asegura de que se agregue un valor válido
    multivar = int(input("Ingresa un número entre 0 y 255: "))

multivar=format(multivar,"08b")     #Se convierte a binario con un 8 valores

print("Bits activados:")
for i in range(8):
    if multivar[7-i] == '1':
        print(lista[i])



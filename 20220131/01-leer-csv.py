#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later


nombre = input("Escribe el nombre del archivo a leer: ")

archivo = open(nombre)
contador = 0

for linea in archivo:
    lista = linea.split(",")
    contador = 0
    for valor in lista:
        print("v{}".format(contador)," = ",valor.strip(),end="; ")
        contador += 1
    print()

archivo.close()
        


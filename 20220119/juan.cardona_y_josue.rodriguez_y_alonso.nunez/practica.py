#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de un modulo
"""
import os

nombre = input("Introduzca el nombre del archivo a copiar: ")
nombre_copia = nombre.strip('.txt')

if os.path.exists(nombre):
    f = open(nombre, 'r')
    f1 = open(nombre_copia+"-copia.txt", 'w')
    f1.write(f.read())
    f1.close()
    print(f'copie el contenido de {nombre}, en {nombre_copia}-copia.txt')   
    f.close()
else:
    print("el archivo no existe")

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

nombre = input('Introduzca el nombre del archivo a copiar: ')
nombre_copia = nombre.strip('.txt')

if os.path.exist(nombre):
    f = open(f'{nombre}', 'r')
    f.close()
    f1 = open(f'{nombre_copia}', 'a')
    f1.write(f'{f}')
    f1.close()

    print(f'copie el contenido de {nombre}, en |')
else:
    #archivo no existe


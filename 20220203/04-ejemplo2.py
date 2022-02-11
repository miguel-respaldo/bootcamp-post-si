#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

import os

nombre = input("Escribe el nombre del archivo: ")

try:
    f = open(nombre)
    try:
        f.write("Algo\n")
    except:
        print("mmm.. algo salio mal")
    finally:
        f.close()
except:
    print("No se pudo abrir el archivo")


if os.path.exists(nombre):
    f = open(nombre,"a")
    f.write("Algo más\n")
    f.close()
else:
    print("el archivo con nombre", nombre,"no existe")




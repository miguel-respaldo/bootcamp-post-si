#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

archivo = open("demo2.txt", "a")

archivo.write("Linea 1\n")
archivo.write("Linea 2\n")
archivo.write("Linea 3\n")

archivo.close()

archivo = open("demo2.txt", "a")

archivo.write("Linea 4\n")
archivo.write("Linea 5\n")
archivo.write("Linea 6\n")

archivo.close()

archivo = open("demo2.txt", "r")
print(archivo.read())
archivo.close()

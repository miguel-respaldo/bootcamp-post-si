#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

archivo = open("demo3.txt", "w")
archivo.write("Borrado 1\n")
archivo.write("Borrado 2\n")
archivo.write("Borrado 3\n")
archivo.close()

archivo = open("demo3.txt", "r")
print(archivo.read())
archivo.close()

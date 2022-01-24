#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

archivo = open("/proc/cpuinfo")

for linea in archivo:
    if "spectre" in linea:
        lista = linea.split(" ")
        for palabra in lista:
            if palabra != "":
                print(palabra)

archivo.close()

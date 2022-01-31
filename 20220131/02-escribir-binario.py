#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later


nombre = input("Escribe el nombre de salida: ")

baits = bytearray(7)

baits[0]=11
baits[1]=14
baits[2]=11
baits[3]=14
baits[4]=ord(" ")
baits[5]=0xBE
baits[6]=0xBE

archivo = open(nombre,"wb")
archivo.write(baits)
archivo.close()
        

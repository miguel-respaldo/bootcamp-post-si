#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Proyecto
"""
import os

def main():

    programa = input("Introduzca el nombre del programa MIPS: ")

    if os.path.exists(programa):
        f = open(programa, 'r')
        
        f.close()
    else:
        print("El archivo no existe")

    print("Ya estas dentro de proyecto")
if __name__ == "__main__":
    main()

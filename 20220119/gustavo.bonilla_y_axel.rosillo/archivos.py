#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
    Práctica de archivos
"""

import os.path

def main():
    original = "demo.txt"
    original = input("\nIntrodusca el nombre del archivo a copiar: ")
    copia = original + "copia.txt"

    if os.path.isfile(original):
        archivo = open(original, "r")
        texto = archivo.read()

        print("\n###### Contenido del archivo: ######")
        print(texto)
        print("####################################\n")
        
        archivo_copia = open(copia, "w")
        archivo_copia.write(texto)  
        
        archivo.close()
        archivo_copia.close()
    else:
        print("\nERROR: Archivo solicitado no existe:(\n")


if __name__ == "__main__":
    main()


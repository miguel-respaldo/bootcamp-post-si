#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Practica de archivos
"""

def main():
    original="demo.txt"
    copia="demo-copia.txt"

    archivo = open(original,"r")
    print(archivo.read())
    texto=archivo.read()
    
    
    

    
    archivo_copia = open(copia,"a")
    for linea in archivo:
        archivo_copia.write(linea.strip())
        
    archivo.close()
    archivo_copia.close()

if __name__ == "__main__":
    main()


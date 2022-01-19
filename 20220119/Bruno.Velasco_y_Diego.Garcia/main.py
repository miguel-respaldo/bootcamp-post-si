#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de un modulo
"""
from os import path

def añadirCopiaAlFinal(arg):
    new = arg.split('.')
    indexPunto = len(new)
    new.insert(indexPunto-1," - copia.")
    
    final = ""
    for i in new:
        final += i
    
    return final



def main():
    nombre = input("Ingrese el nombre del archivo a copia: ")
    
    if path.exists(nombre):
        archivo = open(nombre, 'r')
        
        new = añadirCopiaAlFinal(nombre)
        
        copia = open(new, 'w')
        copia.write(archivo.read())

        print("Archivo copiado en ...")

        archivo.close()
        copia.close()
    else:
        print("Archivo inexistente :/")


if __name__ == "__main__":
    main()


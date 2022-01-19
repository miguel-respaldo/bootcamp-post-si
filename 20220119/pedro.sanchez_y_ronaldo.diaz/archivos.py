#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Este programa es para crear y copiar un archivo
"""

def main(): 
    #print("Hola Mundo")
    
    f = input("Introduce el nombre del archivo (con extension) a copiar: ")
    
    ext="_copy.txt"
    nom=f[:f.index('.')]
    nombre=nom+ext

    demo = open(f, "rt") 
    a = demo.read()
    demo.close()
    
    archivo = open(nombre, "w") # para que reescriba si existe
    archivo.write("\nEste es el archivo que se crea con el contenido \n")
    archivo.write("del archivo ingresado: \n")
    archivo.write(a)
    archivo.close()
    
    demo = open("ejemplo.txt","rt")
    print(demo.read())
    demo.close()

if __name__ == "__main__":
    main()


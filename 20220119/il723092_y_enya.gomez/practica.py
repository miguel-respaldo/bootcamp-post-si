#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de un modulo
"""

def main():
    """
    Comentario de la función
    """
    f = input("Introduce el nombre del archivo a copiar: ")
    archivo1 = open( f+'-copia.txt', 'w')
    archivo2 = open( f+".txt" , "r")
    archivo1.write(archivo2.read())
    
    archivo1.close()
    archivo2.close()

    archivo1 = open( f+'-copia.txt', 'r')
    print(archivo1.read())

if __name__ == "__main__":
    main()


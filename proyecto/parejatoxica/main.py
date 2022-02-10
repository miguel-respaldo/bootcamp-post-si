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
    
    #--------------------- LEE EL ARCHIVO Y TIPO DE SALIDA --------------------
    archivo = input("Introduzca el nombre del programa MIPS: ")
    while not os.path.exists(archivo):
        archivo = input("El archivo no existe, introduzca otro nombre: ")
    
    print("\nPuedes obtener el archivo de salida en:\n(1)-Texto\n(2)-Binario")
    salida = int(input("Indica el tipo de salida del programa: "))
    while not (salida==1 or salida==2):
        salida = int(input("Tipo de salida invalido, vuelve a intentar: "))
        
    print("Ya estas dentro de proyecto")

    
    #---------------------- GUARDAR CADA INSTRUCCION --------------------------
    programa = open(archivo,'r')
    contador = 0

    for linea in programa:
        lista = linea.split(",")
        contador = 0
        for valor in lista:
            print("V{}".format(contador),"=",valor.strip(),end=("/"))
            contador += 1
        print()
    
    programa.close


if __name__ == "__main__":
    main()

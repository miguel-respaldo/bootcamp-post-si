#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Practica 2: Varianza
"""
import math


def main():
    suma=0
    lista=[]
    for i in range(0,7):
        cont = float(input("Ingrese un numero: "))
        lista.append(cont)
        
    #lista = [2,4.6,3.6,2.4,7.6,8.9,10]
    
    for i in lista:
        suma = suma + i     # Hace la suma de elementos

    media = suma/len(lista) # Determina la media
    
    sumatoria=0
    for i in lista:
        sumatoria = sumatoria + ( ( i - media ) ** 2 ) # Hace la sumatoria

    varianza = sumatoria / ( len(lista) - 1 )   # Calcula la varianza

    print(varianza)



    

  
    
    
    
if __name__ == "__main__":
    main()


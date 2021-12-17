#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Practica 1
"""
import cmath
import math

def main():

    a = float(input("Introduzca a:")) 
    b = float(input("Introduzca b:"))
    c = float(input("Introduzca c:"))
    
    r=(b ** 2)-(4 * a * c)          #se realiza la operación dentro de la raiz
    if r<0: 
       x1 = - b + cmath.sqrt ( r ) / ( 2 * a ) #se encuentra la primer sol. x1
       x2 = - b - cmath.sqrt ( r ) / ( 2 * a ) #se encuentra la segunda sol. x2
    else: 
       x1 = - b + math.sqrt ( r ) / (2 * a) #primer solución real x1
       x2 = - b - math.sqrt ( r ) / (2 * a) #segunda solucion real x2
    print("El resultado de x1 es:",x1)
    print("El resultado de x2 es:",x2)

if __name__ == "__main__":
    main()
    

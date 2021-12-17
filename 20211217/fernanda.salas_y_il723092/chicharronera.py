#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
#from math import sqrt 
import math

a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
c = int(input("Ingrese el valor de c: "))  

x1 = 0
x2 = 0

disc = b**2 -4*a*c

if (disc) < 0:
    print("Ecuación con números complejos")
    c1 = complex(-b/(2*a),math.sqrt(-1*disc/(2*a))
    c2 = complex(-b/(2*a),-1*math.sqrt(-1*disc/(2*a))
    
    print("El resultado complejo en x1 es:",c1.real,"+",c1.imag,"j")
    print("El resultado complejo en x2 es:",c2.real,"-",-1*c2.imag,"j")

else:
    x1 = (-b + math.sqrt(disc)/(2*a)
    x2 = (-b - math.sqrt(disc)/(2*a)

    print("El resultado en x1 es:",x1)
    print("El resultado en x2 es:",x2)


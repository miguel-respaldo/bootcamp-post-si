#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Ejemplo de un modulo
"""

import math

def main():
    """
    Comentario de la función
    """
    ind = True
    while ind:
        ind = False
        a= int(input("ingresa A: "))
        if a == 0:
            ind = True
            print("a debe ser diferente de cero, vuelve a intentarlo")
    b= int(input("ingresa B: "))
    c= int(input("ingresa C: "))
    x1=0
    x2=0
    x1i=0 + 0j
    x2i=0 + 0j
    comparacion = (b**2)-4*a*c
    if (comparacion<0):
        comparacion = abs(comparacion)
        comparacion = math.sqrt(comparacion)
        x1i=complex(-b,comparacion)
        x2i=complex(-b,-comparacion)
        print("Valor de x1: {}".format(x1i/(2*a)))
        print("valor de x2: {}".format(x2i/(2*a)))
    else:
        x1= (-b+math.sqrt(comparacion))/(2*a)
        x2= (-b-math.sqrt(comparacion))/(2*a)
        print("Valor de x1: {}".format(x1))
        print("valor de x2: {}".format(x2))




if __name__ == "__main__":
    main()

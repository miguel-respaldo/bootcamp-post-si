#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de un modulo
"""

from math import sqrt

def main():
    """
    Comentario de la función
    """
    a= int(input("ingresa A: "))
    b= int(input("ingresa B: "))
    c= int(input("ingresa C: "))
    x1=0
    x2=0

    if ((b**2)-5*a*c)<0:
        print("la solucion es con num complejos")
    else:
        x1= (-b+sqrt(b**2-(4*a*c)))/(2*a)
        x2= (-b-sqrt(b**2-(4*a*c)))/(2*a)

    print("Valor de x1: {}".format(x1))
    print("valor de x2: {}".format(x2))




if __name__ == "__main__":
    main()


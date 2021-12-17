#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Práctica 1: Fórmula General para Ecuaciones Cuadráticas
"""
import math
from cmath import sqrt

def main():
    a = float(input ('Introduzca a:'))
    b = float(input ('Introduzca b:'))
    c = float(input ('Introduzca c:'))

    aux_1 = (b**2)-(4*a*c)

    if(aux_1) < 0:
        print("Solución con el uso de números complejos:")
        aux_1 = sqrt(aux_1)
    else:
        print("Solución sin el uso de números complejos:")
        aux_1 = math.sqrt(aux_1)
    
    x1 = (-b+aux_1) / (2*a)
    x2 = (-b-aux_1) / (2*a)
    
    print(x1)
    print(x2)
    

if __name__ == "__main__":
    main()


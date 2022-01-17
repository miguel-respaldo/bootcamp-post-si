#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

import operaciones

def principal():
    """
    Practica: Fibonacci y Factorial
    """
    
    '''
    n1 = eval(input("Escribe un número: "))
    n2 = eval(input("Escribe otro número: "))

    res = suma(n1, n2)
    print(f"El resultado es: {res}")
    res = operaciones.resta(n1, n2)
    print(f"El resultado es: {res}")
    res = operaciones.multiplicacion(n1, n2)
    print(f"El resultado es: {res}")
    res = operaciones.division(n1, n2)
    print(f"El resultado es: {res}")
    '''

    n = eval(input("Introduce el numero para Fibonacci: "))
    #fibonacci(n)

if __name__ == "__main__":
    principal()


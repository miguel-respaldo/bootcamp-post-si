#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de un modulo
"""

import operaciones

def main():

    n1 = eval(input("Inserte el número para la Sucesión Fibonacci: "))
    if n1 <=0:
        print("Ingrese un entero positivo: ")
    else:
        print("Sucesión de Fibonacci: ")
    for i in range(n1):
        print(operaciones.fibonacci(i))

if __name__ == "__main__":
    main()

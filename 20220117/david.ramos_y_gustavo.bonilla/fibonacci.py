#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
    Fibonacci
"""

from funciones import fibonacci_2

def main():
    """
        Ejecución de fibonacci
    """
    
    print("\nHola!!, Este script calcula la función de Fibonacci de un número.")
    num = eval(input("\nIntroduce el número al que desceas aplicar la función de Fibonacci: "))
    print(f"\nLa posición {num} de fibonacci es: {fibonacci_2(num)}\n")


if __name__ == "__main__":
    main()

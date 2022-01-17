#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
    Factorial
"""

from funciones import factorial

def main():
    """
        Ejecución de factorial
    """

    print("\nHola!!, Este script calcula el facorial de un número.")
    num = eval(input("\nIntroduce el número del que desceas su factorial: "))
    print(f"\nEl resultado es: {factorial(num)}\n")


if __name__ == "__main__":
    main()

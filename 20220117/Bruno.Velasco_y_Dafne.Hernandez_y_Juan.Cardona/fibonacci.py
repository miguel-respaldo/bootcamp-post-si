#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de un modulo
"""
#print(fib(8))

import operaciones

def main():
    """
    y van muy bien con cafe en la noche
    """
    n = int(input("Ingrese un numero para fibonacci: "))

    res = operaciones.fib(n)
    print(res)


if __name__ == "__main__":
    main()

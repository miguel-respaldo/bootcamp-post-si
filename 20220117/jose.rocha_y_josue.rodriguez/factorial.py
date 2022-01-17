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
    
    n1=eval(input("Inserte el factorial:"))
    res=operaciones.factorial(n1)
    print ("El resultado de {} factorial es: {}".format(n1,res))

if __name__ == "__main__":
    main()


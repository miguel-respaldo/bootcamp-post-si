#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de un modulo
"""
def fibonacci(n): 
    if n <=1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))

nterminos=10 #nota: cambiarlo para ponerle un input

#checando que el número de términos es válido
if nterminos <=0:
    print("Ingrese un entero positivo: ")
else:
    print("Sucesión de Fibonacci: ")
for i in range(nterminos):
    print(fibonacci(i))


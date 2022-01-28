#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

def f1(funcion):
    def wrapper(*args, **kwargs):
        print("Inicia función")
        res = funcion(*args, **kwargs)
        print("Termina función")
        return res

    return wrapper


@f1  # suma = f1(suma)
def suma(a, b):
    return a + b

@f1
def sumavarios(*args):
    res = 0
    for num in args:
        res +=num

    print(res)

resultado = suma(3,4)

print("El resutaldo es:", resultado)

#r = sumavarios(1,2,3)
#print("El r es:", r)
sumavarios(1,2,3,4)

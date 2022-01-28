#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

def f1(funcion):
    def wrapper(*args):
        print("Bienvenido")
        funcion(*args)
        print("Vuelve pronto")

    return wrapper

@f1
def suma(a, b):
    print("La suma de",a,"y",b,"es:",a+b)



def sumados(*args):
    print("La suma de",args[0],"y",args[1],"es:",args[0]+args[1])


@f1
def sumavarios(*args):
    res = 0
    for num in args:
        res +=num

    print(res)


#suma(3,4)
sumavarios(1,2,3,4)

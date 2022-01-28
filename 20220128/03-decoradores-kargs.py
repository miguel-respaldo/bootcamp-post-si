#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

def f1(funcion):
    def wrapper(*args, **kwargs):
        print("Bienvenido")
        funcion(*args, **kwargs)
        print("Vuelve pronto")

    return wrapper


@f1
def suma(a, b):
    print("La suma de",a,"y",b,"es:",a+b)

@f1
def sumavarios(*args):
    res = 0
    for num in args:
        res +=num

    print(res)

@f1
def suma3(a, b, c):
    print(f"{a} + {b} + {c} = {a+b+c}")

def sumados(**kwargs): # keyword arguments
    print("La suma de",kwargs["primero"],"y",kwargs["segundo"],"es:",kwargs["primero"]+kwargs["segundo"])


#sumados(segundo=3, primero=5)
#suma(b=5,a=3)
#suma(8,2)
#suma(15, b=5)
sumavarios(1,2,3,4)
suma3(3,4,3)
suma3(1,c=3,b=2)



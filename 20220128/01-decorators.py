#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

def e():
    print("Hola")

def f1(funcion):
    def wrapper():
        print("Bienvenido")
        funcion()
        print("Vuelve pronto")

    return wrapper

@f1
def f():
    print("Hola Mundo")

@f1
def d():
    print("Saludos")


e = f1(e)
e()

#cualquier_nombre = f1(d)
#cualquier_nombre()

#f = f1(f) #  --> @f1
#f()

#d = f1(d) #  --> @f1
#d()




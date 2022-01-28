#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

import datetime
import time

def log(funcion):
    def wrapper(*args, **kwargs):
        f = open("log.txt","a")
        f.write("La función con argumentos: " + " ".join([str(arg) for arg in args]) + " fue llamada  a las " + str(datetime.datetime.now()) + "\n")
        f.close()
        res = funcion(*args, **kwargs)
        return res

    return wrapper


@log
def suma(a,b):
    return a+b

@log
def resta(a,b):
    return a-b


res = suma(3,4)
time.sleep(2)
print("El resultado es: ", res)
res = resta(5,2)
print("El resultado es: ", res)
time.sleep(1)
res = suma(1000,20000)
print("El resultado es: ", res)

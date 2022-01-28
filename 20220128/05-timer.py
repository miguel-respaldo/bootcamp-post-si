#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

import time

def timer(funcion):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        funcion(*args, **kwargs)
        fin = time.time()
        return fin - inicio

    return wrapper


@timer
def dormir(segundos):
    print("Inicia")
    for s in range(segundos):
        time.sleep(1)
        print(".")

    print("Termina")


tiempo = dormir(5)
print("Se tardo", tiempo, "segundos")


#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

def mi_funcion(n3,n2,n1):
    print(f"n3 = {n3}")
    print(f"n1 = {n1}")
    print(f"n2 = {n2}")


#mi_funcion(n3="uno", 2, "algo") # marca error

mi_funcion("uno", n1=2, n2="algo")

print("sin salto de linea", end="")
print("+++")


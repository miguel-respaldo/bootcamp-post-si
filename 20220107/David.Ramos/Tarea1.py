#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

num = format(int(input("Ingresa un numero entre 0 y 255: ")),"b")
Cosas = ["Casa","Perro","Gato","Pez","Moto","Zapato","Navidad"]
if num == "0":
    print("Nada que hacer")
    
else:
    i = len(num) - 1
    for x in num:
        if x == "1" : print(Cosas[i])
        i -= 1

#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

num = format(int(input("Ingresa un numero entre 0 y 255: ")),"b")

if num == "0":
    print("Nada que hacer")
    
else:
    iterador = len(num)
    for x in num:
        if x == "1":
            if iterador == 1:
                print("Casa")
            elif iterador == 2:
                print("Perro")
            elif iterador == 3:
                print("Gato")
            elif iterador == 4:
                print("Pez")
            elif iterador == 5:
                print("Moto")
            elif iterador == 6:
                print("Zapato")
            elif iterador == 7:
                print("Navidad")
        iterador -= 1

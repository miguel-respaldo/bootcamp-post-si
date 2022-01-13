#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""

Ejercicio donde una variable puede contener varias en su valor y se compara
cuales se encuentran presentes.

"""
import random

def main():
    multivariable = 0
    cant=random.randrange(1,8)
    for i in range(cant):
        randVal = 2**(random.randrange(0, 8))
        multivariable += randVal 

    carro=1
    casa=2
    perro=4
    gato=8
    pez=16
    moto=32
    zapato=64
    navidad=128

    if multivariable & carro:
        print('Carro presente')

    if multivariable & casa:
        print('Casa presente')

    if multivariable & perro:
        print('Perro presente')

    if multivariable & gato:
        print('Gato presente')

    if multivariable & pez:
        print('Pez presente')

    if multivariable & moto:
        print('Moto presente')

    if multivariable & zapato:
        print('Zapato presente')

    if multivariable & navidad:
        print('Navidad presente')

    print('La variable entera con las booleanas es: {} '.format(multivariable))


if __name__ == "__main__":
    main()


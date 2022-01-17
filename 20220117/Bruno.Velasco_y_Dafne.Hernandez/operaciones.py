#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# SPDX-License-Identifier: GPL-3.0-or-later

def suma(n1, n2):
    return n1 + n2


def resta(n1, n2):
    return n1 - n2


def multiplicacion(n1, n2):
    return n1 * n2


def division(n1, n2):
    if n2 == 0:
        return 0
    return n1 / n2


if __name__ == "__main__":
    print("Este es un modulo, no un programa")

#print("***** Este es un modulo, no un programa +++++")



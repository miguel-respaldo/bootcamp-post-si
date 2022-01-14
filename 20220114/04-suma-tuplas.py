#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# SPDX-License-Identifier: GPL-3.0-or-later


tupla = ("manzana", "platano", "naranja")
print("Tupla 1:", tupla)

tupla_varios_datos = ("abc", 33, True, 3.1416, "def")
print("Tupla 2:", tupla_varios_datos)

tupla_3 = tupla + tupla_varios_datos

print("Tupla 1 + Tupla 2:", tupla_3)


#tupla = ("manzana", "platano", "naranja")
#tupla2 = ("manzana", "platano", "naranja")
#tupla -= tupla2
# unsupported operand type(s) for -=: 'tuple' and 'tuple'

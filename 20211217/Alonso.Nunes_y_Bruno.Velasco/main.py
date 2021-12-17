#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

import math
import cmath

a = int(input("Introduzca valor para A: "))
b = int(input("Introduzca valor para B: "))
c = int(input("Introduzca volor para C: "))

b4ac = (b ** 2 - 4 * a * c)

if (b4ac > 0):
    sqr = sqrt(b4ac)
    z1 = (-b + sqr) / (2 * a)
    z2 = (-b - sqr)
else:
    b4ac = b4ac * -1
    z1 = (-b + complex(0, sqr)) / (2 * a) 
    z2 = (-b - complex(0, sqr)) / (2 * a)

print(z1.real)
print(z1.imag)
print(z2.real)
print(z2.imag)

print("El valor para z1 es =", z1)
print("El valor para z2 es =", z2)


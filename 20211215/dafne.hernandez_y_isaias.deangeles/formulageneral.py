#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de un modulo
"""

import math

a = float(input('Indica el valor de a: '))
b = float(input('Indica el valor de b: '))
c = float(input('Indica el valor de c: '))

raiz = math.sqrt((b*b) - 4*(a*c))
div = 2*a

x1 = (-b + raiz) / div
x2 = (-b - raiz) / div

print('El valor de x1 es:', x1)
print('El valor de x2 es:', x2)

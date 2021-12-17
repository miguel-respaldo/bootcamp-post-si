#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later


a= float(input('Ingresa el valor de a:  '))
b= float(input('Ingresa el valor de b:  '))
c= float(input('Ingrese el valor de c:  '))

x1=(-b+(((b**2)-(4*a*c))**0.5))/(2*a)
x2=(-b-(((b**2)-(4*a*c))**0.5))/(2*a)

print('el valor de x1 es: ')
print(x1)

print('el valor de x2 es: ')
print(x2)

if a==0:
    print('no puede ser 0')

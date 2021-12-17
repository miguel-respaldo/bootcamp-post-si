#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

#solicitar datos de entrada a, b, c de la ecuacion cuadratica
a= float(input('Ingresa el valor de a:  ')) 
b= float(input('Ingresa el valor de b:  '))
c= float(input('Ingrese el valor de c:  '))

x1=(-b+(((b**2)-(4*a*c))**0.5))/(2*a ) #calculo de x1
x2=(-b-(((b**2)-(4*a*c))**0.5))/(2*a) #calculo de x2

print('el valor de x1 es: ')
print(x1) #imprime x1

print('el valor de x2 es: ')
print(x2) #imprime x2

if a==0:
    print('no puede ser 0') # si a=0, el valor es infinito

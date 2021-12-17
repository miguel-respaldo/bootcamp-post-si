#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

from math import sqrt

print('Este programa es para resolver una ecuación de segundo grado:')
print('ax² + bx + c = 0\n')

# Se solicitan datos al usuario
a = float(input("Ingresa el valor de a: "))
b = float(input("Ingresa el valor de b: "))
c = float(input("Ingresa el valor de c: "))

print('Ingresaste la ecuacion:', a,'x² +',b,'x +',c,'c = 0\n')

# Se calcula el determinante
det = (b*b) - (4*a*c)

if det < 0: # comprobamos si no existen soluciones reales
    print('La ecuación contiene numeros imaginarios')

else:
    x1 = ((-b + sqrt(det)) / (2*a))     # se calcula la primera solucion

    if det != 0:                        # para saber si hay otra solucion
        x2 = (-b - sqrt(det)) / (2*a)   # calculamos la segunda solución
        print(f'Las soluciones son {x1} y {x2}') # mostramos las dos soluciones
    else:
        print(f'La única solución es x = {x_1}') # mostramos la única solución



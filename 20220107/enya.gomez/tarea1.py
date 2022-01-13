#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
tarea 1
"""

d=  [["Carro", 1,"0000 0001"],
    ["Casa", 2, "0000 0010"],
    ["Perro", 4, "0000 0100"],
    ["Gato", 8, "0000 1000"],
    ["Pez", 16, "0001 0000"],
    ["Moto", 32, "0010 0000"],
    ["Zapato", 64,"0100 0000"],
    ["Navidad", 128, "1000 0001"]]


print ("{:<10} {:<10} {:<10}".format("Variables", "Decimal", "Bool"))
for v in d:
	Variables, Decimal, Bool = v
	print("{:<10} {:<10} {:<10}".format( Variables, Decimal, Bool))
dato = int( input ("Ingresa un valor de 0 a 255:  "))
dato1 = dato
val = "{0:08b}".format(dato)
print (val)

if dato1 == 1:
	print ('Mi hermano choco el carro\n')

if dato1 == 2:
        print ('Mi casa es muy fría\n')

if dato1 == 4:
        print ('Mi perro rompio un plato\n')

if dato1 == 8:
        print ('El gato llevo un pajaro\n')

if dato1 == 16:
        print ('Pato es un pez (Lilo)\n')

if dato1 == 32:
        print ('La moto se destruyo\n')

if dato1 == 64:
        print ('Mi zapato es de color rosa\n')

if dato1 == 128:
        print ('La navidad incluye mucho dinero\n')

#00000000  =  0
#00000010  =  2  -> Casa
#10001001  =  137  -> carro on, gato on, navidad on

#multivariable = int(0)

#carro = 1
#navidad = 128

#si multivariable  = carro hacer
 # algo

#si multivariable = navidad hacer
 # otra cosa


#si multivariable = carro y multivariable = pez y multivariable = navidad hacer
 #un carro conducido por un pez en navidad
#

#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-late
'''
Hacer un programa que guarde hasta 8 variables booleanas en un entero.

'''
#declaramos la lista con las palabras
variables = ["Carro", "Casa", "Perro", "Gato", "Pez", "Moto", "Zapato", "Navidad"]

#solicitamos los numeros enteros
multivariable = int(input("Ingrese un numero entero: "))
bin = "{:b}".format(multivariable)#convertimos los enteros a binario
print(bin) #imprimimos el numero binario

for i in range(8):
    if bin[i] == "1":
        print(variables[i], "on,", end=" ")
    else:
        print(variables[i], "off,", end=" ")

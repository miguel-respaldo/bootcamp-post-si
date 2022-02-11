#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

def division(num1, num2):
    return num1 / num2


def lectura(cadena):
    esNumero = False
    numero = 0
    #while esNumero == False:
    while not esNumero:
        entrada = input(cadena)
        try:
            numero = eval(entrada)
        except:
            print("Ese no es un número:")
        else:
            esNumero = True
    return numero

numero1 = lectura("Escribe un número: ")

numero2 = 0
while  numero2 == 0:
    numero2 = lectura("Escribe un número diferente de cero: ")


try:
    resultado = division(numero1, numero2)
except:
    print("no se puede dividir entre cero")
else:
    print("La división es:", resultado)



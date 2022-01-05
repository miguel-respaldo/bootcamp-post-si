#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later


print("Programa para calculo de varianza") 
print("ingrese 7 valores")

lista = [0,0,0,0,0,0,0] #se crea lista con 7 posiciones
promedio = 0
sumatoria = 0

for x in range(7):
    lista[x] = input("Ingresa el valor {}:  ".format(x+1)) #se llena la lista con los datos ingresados por el usuario

for x in lista:
    promedio += int(x) # se suman los 7 valores
    
promedio /= 7 # se calcula el promedio de los 7 valores

for x in lista:
    sumatoria += ((int(x) - promedio) ** 2) # se calcula la varianza
    
print("La varianza es {}".format(sumatoria / 6))

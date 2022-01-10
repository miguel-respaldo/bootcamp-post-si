#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later


print('''
las variables disponibles son:

variable        binario         decimal
Carro                 1               1
Casa                 10               2
Perro               100               4
Gato               1000               8
Pez               10000              16
Moto             100000              32
Zapato          1000000              64
Navidad        10000000             128
''')

multiv = int(input('Ingrese un numero igual o menor a 255: '))#Solicitando numero
multiv_binario = format(multiv, '08b') #Convertir entero a binario formato 8 bit
objetos = ['Carro', 'Casa', 'Perro', 'Gato', 'Pez', 'Moto', 'Zapato', 'Navidad']
#Lista con elementos disponibles
contador_r = 0 #Contador necesario para que los elementos concuerden con el 
               #numero ingresado por el usuario

if multiv > 255: #definiendo rango minimo de operacion
    print('Valor fuera de rango, intentelo de nuevo')
else:
    print('Los objetos encontrados son:') 
    for x in range(8): #recorriendo el multiv_binario bit a bit
        contador_r -= 1 #Decrementa para imprimir los valores correctamente
        if (int(multiv_binario[x]) == 1): #Si el valor actual de multiv es 1,
            print(objetos[contador_r], 'on')    #imprime el objeto de la lista


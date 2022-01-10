#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de bits
"""

lista="""
      objeto        valor decimal    valor binario
      carro     =        1             00000001
      casa      =        2             00000010
      perro     =        4             00000100
      gato      =        8             00001000
      pez       =        16            00010000
      moto      =        32            00100000
      zapato    =        64            01000000
      navidad   =        128           10000000
"""
print(lista)

multivariable=int(input("Inserte un número entero menor o igual a 128:"))
mulbin=format(multivariable,"08b") #convertimos el numero insertado a binario
cadena=str(mulbin)                 #convertimos el binario a cadena

print("valor de tu numero en decimal",multivariable)
print("valor de tu numero en binario:", mulbin)

#hacemos un arreglo con los objetos a imprimir
cosas=["navidad","zapato","moto","pez","gato","perro","casa","carro"] 


for i in range(8):
    if int(cadena[-i])==0:   #tomamos la cadena para verificar cada elemento binario
       pass        
    elif multivariable>128:  #si la variable de entrada es mayor a 128 termina el proceso
        print("Número fuera de rango proceso terminado")
        break
    else:                    #imprime los objetos activos
        print("Está activado:",cosas[-i])
    

#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejercicio de bits condicionales
"""

def main():
    resto=list()    #Guardar los resto de modulo, numero binario o bander
    Menu = ''' Bienvenido a su casa inteligente que desea activar\n
           Carro                  -> 1\n
           Moto                   -> 2\n
           Porton electrico       -> 4\n
           Puerta                 -> 8\n
           Luces hogar            ->16\n
           Aire Condicionado      ->32\n
           Television             ->64\n
           Luces Navidennas       ->128\n '''
    print(Menu)
    Multivariable = int(input("\nIntroduce un numero del 0 al 255\n"))

#cambiar el numero decimal a binario para usarlo como bandera en cada posicion 
    while Multivariable != 0: # Hacer mientras el número de sea diferente de cero
        resto.append(Multivariable %2) # guardamos el módulo calculado en orden 
        Multivariable //=2  #asignar el nuevo valor despues de la division 
        #print(resto)
       #print(len(resto))

    for i in range (len(resto)):
        if resto[0] == 1:               #bit menos significativo 
            print('Se encendio el carro\n')
        if resto[1] == 1:
            print('Se encendio la moto\n')
        if resto[2] == 1:
            print('Se abrio el porton electrico\n')
        if resto[3] == 1:
            print('Se abrio la puerta principal\n')
        if resto[4] == 1:
            print('El encendio las luces\n')
        if resto[5] == 1:
            print('Se activo el aire condicionado\n')
        if resto[6] == 1:
            print('Se encendio la Television\n')
        if resto[7] == 1:               #bit mas significativo 
            print('Se activaron las luces navidennas\n')

if __name__ == "__main__":
    main()


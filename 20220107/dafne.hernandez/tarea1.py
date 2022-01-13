#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

varBool = ['Carro', 'Casa', 'Perro', 'Gato', 'Pez', 'Moto', 'Zapato', 'Navidad']
valido = False 
indicevar=-1; #para coincidir a varBool con el numero ingresado

while not valido:
    multivariable = int(input('Ingresa un numero (1-255): '))
    print(multivariable)
    if multivariable >= 1 and multivariable <= 255:
        valido = True;
    if not valido:
        print('Lo siento, el valor no es válido, vuelva a intentarlo: ', end='')

multivariable = format(multivariable, "b"); #modifico a binario

print("El numero en binario es:  ", multivariable)
for x in range(7,-1,-1): #recorrer de 8 en 8 al revés 
        indicevar+=1; #este controla que imprima poniendo el indice correcto desde 0 hasta 7
        #1 ---- 0 (indicevar)
        #0 ---- 1
        #0 ---- 2
        #1 ---- 3
        #0 ---- 4
        #0 ---- 5        
        #0 ---- 6
        #1 ---- 7
        #print("k ", multivariable[x]) #checar que imprima cómo está letendo
        if (int(multivariable[x]) == 1): #Si el bit es 1 
        #entonces se imprime en la posicion actual de indicevar el elemento.
            print(varBool[indicevar], 'on')    #imprime el de esa posición
            if (varBool[indicevar] == 'Carro'):
                  print("Coche prendido")
            if (varBool[indicevar] == 'Casa'):
                  print("Luces de la casa prendidas")
            if (varBool[indicevar] == 'Perro'):
                  print("El perro te saluda")
            if (varBool[indicevar] == 'Gato'):
                  print("El gato escapo de nuevo")
            if (varBool[indicevar] == 'Pez'):
                  print("Buscando a Nemo")
            if (varBool[indicevar] == 'Moto'):
                  print("Las luces de la moto se prendieron")
            if (varBool[indicevar] == 'Zapato'):
                  print("Tu zapato se rompio")
            if (varBool[indicevar] == 'Navidad'):
                  print("Se enciendieron las luces del arbol")


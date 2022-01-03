#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de un modulo
"""

def main():

    numeros=[]              # se declara una lista vacia
    varianza=0              # se declara variable de varianza
#    sumatoria=0             # sumatoria auxiliar
#    n=0                     # cantidad de numeros a ingresar

    print("Este programa obtiene la varianza")
    n=int(input("Ingresa la cantidad de numeros para obtener la varianza: "))

    for x in range(n):  # se hace un for para obtener los 7 valores
        dato=int(input("Ingrese el numero: "))
        numeros.append(dato) #agrega los elementos a la lista
        
    mean = sum(numeros) / n

    #for x in range(n):
       #suma = (numeros[x]-mean)**2 

    varianza = sum((x-mean)**2 for x in numeros) / (n-1)
    #varianza = (1/(n-1)) * suma
    print("\nLa varianza es:",varianza)

if __name__ == "__main__":
    main()

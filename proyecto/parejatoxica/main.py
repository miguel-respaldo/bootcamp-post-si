#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Proyecto
"""
import os

def main():
    
    #--------------------- LEE EL ARCHIVO Y TIPO DE SALIDA --------------------
    archivo = input("Introduzca el nombre del programa MIPS: ")
    while not os.path.exists(archivo):
        archivo = input("El archivo no existe, introduzca otro nombre: ")
   
    '''
    print("\nPuedes obtener el archivo de salida en:\n(1)-Texto\n(2)-Binario")
    salida = int(input("Indica el tipo de salida del programa: "))
    while not (salida==1 or salida==2):
        salida = int(input("Tipo de salida invalido, vuelve a intentar: "))
    
    '''
    print("\nYa estas dentro de proyecto\n")

    
    #---------------------- GUARDAR CADA INSTRUCCION --------------------------
    programa = open(archivo,'r')
    contador = 0
    lineas_codigo = 0

    # Crear el archivo para copiar la informacion
    code_output = open("output.txt", "w")    # si existe se reescribe
    code_output.write("\nEste archivo contiene la informacion de tu maquina: \n\n")

    for linea in programa:
        lista = linea.split(",")
        contador = 0
        lineas_codigo += 1
        
        for valor in lista:

            if (valor.find(":") != -1):     # busca si hay etiquetas
                salto = valor.split(":")    # crea un arreglo y separa 
                etiqueta = salto[0]         # el primer elemento es etiqueta
                valor = salto[1]            # el segundo elemento es instruccion
                valor = valor.strip()       # quita espacios
                print(etiqueta,end=(" / "))
                #print("v{}".format(contador),"=",valor,end="; ")

                #mandar llamar funcion
                contador += 1               # aumenta el contador del valor
            else:
                valor = valor.strip()       # quita espacios
                #print("v{}".format(contador),"=",valor,end="; ")

                #mandar llamar funcion
                contador += 1               # aumenta el contador del valor

        print("Esta es la linea:",lineas_codigo)
    print("\nEl codigo tiene:",lineas_codigo)
    
    programa.close()



if __name__ == "__main__":
    main()

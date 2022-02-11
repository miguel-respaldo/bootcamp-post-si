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
import memonicos 

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
    
    #----------------- LEE EL ARCHIVO Y GUARDA CADA LINEA EN LISTAS --------------------------
    programa = open(archivo,'r')
    linea_codigo = 0

    etiqueta = []
    n_etiqueta = []
    lista_linea = []

    for linea in programa:
        contador = 0
        lista_linea.append([])
        lista = linea.split(",")

        for valor in lista:
            
            # Aqui se deben separar las etiquietas de los valores reales
            if (valor.find(":") != -1):     # busca si hay etiquetas
                separador = valor.split(":")    # crea un arreglo y separa 

                etiqueta.append(separador[0]) # guarda etiqueta
                n_etiqueta.append(linea_codigo)  # guarda la linea actual

                valor = separador[1]            # el segundo elemento es instruccion
                valor = valor.strip()           # quita los espacios
            else:
                valor = valor.strip()           # quita los espacios
            
            print("v{}".format(contador),"=",valor,end="; ")
            
            lista_linea[linea_codigo].append(valor)
            contador += 1
        
        print("Esta es la linea:",linea_codigo)
        linea_codigo += 1
    
    print("\nEl codigo tiene:",linea_codigo)
    

    #--------------------- LEE LOS DATOS DEL ARREGLO Y MANDA A SALIDA --------------------
    for linea in lista_linea:
        #print(linea)
        contador = 0

        for valor in linea:
            
            # Obtenemos el tipo de instruccion y su opcode
            if contador == 0:
                type_opcode = memonicos.instruction_decode(valor)   #mandar a llamar funcion
                #print(type_opcode)
                valor = type_opcode[1]       # asignamos el valor del opcode
            
            if valor in etiqueta:
                valor = n_etiqueta[etiqueta.index(valor)]

            #memonicos.write_output(type_opcode,valor)
            print("V",contador,"=",valor,end=("; "))
            contador += 1
        print("")
    
    print("\n")
    print(n_etiqueta)
    print(etiqueta)
    #print(lista_linea)
    programa.close()
    


if __name__ == "__main__":
    main()

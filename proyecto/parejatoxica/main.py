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

    
    #---------------------- GUARDAR CADA INSTRUCCION --------------------------
    programa = open(archivo,'r')
    elemento = 0
    linea_codigo = 0
    etiqueta = []
    n_etiqueta = []
    c_etiqueta = 0
    type_opcode = []

    for linea in programa:
        lista = linea.split(",")
        elemento = 0
        linea_codigo += 1                   # cuenta la linea de codigo actual
        etiqueta.append([])
        n_etiqueta.append([])

        for valor in lista:
            
            # Aqui se deben separar las etiquietas de los valores reales
            if (valor.find(":") != -1):     # busca si hay etiquetas
                separador = valor.split(":")    # crea un arreglo y separa 

                etiqueta[c_etiqueta].append(separador[0]) # guarda etiqueta
                n_etiqueta[c_etiqueta].append(linea_codigo)  # guarda la linea actual
                #print("Etiqueta",etiqueta[c_etiqueta],"en",n_etiqueta[c_etiqueta],end=("; "))
                c_etiqueta += 1

                valor = separador[1]            # el segundo elemento es instruccion
                valor = valor.strip()           # quita los espacios
            else:
                valor = valor.strip()           # quita los espacios
            
            # Obtenemos el tipo de instruccion y su opcode
            if elemento == 0:
                type_opcode = memonicos.instruction_decode(valor)   #mandar a llamar funcion
                #print(type_opcode)
                valor = type_opcode[1]       # asignamos el valor del opcode
            
            # Mandamos el tipo de instruccion y el valor de los registros
            if ((type_opcode[0] == "b") or (type_opcode[0] == "j")):
                memonicos.write_output(type_opcode[0],valor,etiqueta)
            else:
                memonicos.write_output(type_opcode[0], valor)

            #print("v{}".format(elemento),"=",valor,end="; ")

            elemento += 1
        print("Esta es la linea:",linea_codigo)
    print("\nEl codigo tiene:",linea_codigo)
    
    programa.close()
    


if __name__ == "__main__":
    main()

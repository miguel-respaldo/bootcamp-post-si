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
    os.system("clear")

    #--------------------- LEE EL ARCHIVO Y TIPO DE SALIDA --------------------
    archivo = input("Introduzca el nombre del programa MIPS: ")
    while not os.path.exists(archivo):
        archivo = input("El archivo no existe, introduzca otro nombre: ")
       
    print("\nPuedes obtener el archivo de salida en:\n(1)-Texto\n(2)-Binario")
    type_out = int(input("Indica el tipo de salida del programa: "))
    while not (type_out==1 or type_out==2):
        type_out = int(input("Tipo de salida invalido, vuelve a intentar: "))
    
    print("\nYa estas dentro de proyecto")
    print("El codigo se guarda en un archivo de salida llamado output.txt\n")
    #----------------- LEE EL ARCHIVO Y GUARDA CADA LINEA EN LISTAS --------------------------
    programa = open(archivo,'r')
    linea_codigo = 0

    etiqueta = []                               # variables para almacenar etiquetas
    n_etiqueta = []
    lista_linea = []

    for linea in programa:
        contador = 0
        lista_linea.append([])
        lista = linea.split(",")

        for valor in lista:
            
            # Aqui se deben separar las etiquietas de los valores reales
            if (valor.find(":") != -1):         # busca si hay etiquetas
                separador = valor.split(":")    # crea un arreglo y separa 

                etiqueta.append(separador[0]) # guarda etiqueta
                n_etiqueta.append(linea_codigo)  # guarda la linea actual

                valor = separador[1]            # el segundo elemento es instruccion
                valor = valor.strip()           # quita los espacios
            else:
                valor = valor.strip()           # quita los espacios
            
            #print("v{}".format(contador),"=",valor,end="; ")
            
            lista_linea[linea_codigo].append(valor) # guarda cada linea de codigo
            contador += 1
        
        #print("Esta es la linea:",linea_codigo)
        linea_codigo += 1
    
    #print("\nEl codigo tiene:",linea_codigo)
    programa.close()                            # cerramos el programa 

    #------------------------------- PROCESAMIENTO DE DATOS ---------------------------
    archivo = open("output.txt","w")
    archivo.close()
    
    linea_codigo = 0
    reorder = []
    
    for linea in lista_linea:
        contador = 0
        reorder.append([])
        
        for valor in linea:
            
            # Obtenemos el tipo de instruccion y su opcode
            if contador == 0:
                valor = memonicos.instruction_decode(valor)   # asigna tipo y opcode
                
            else: 

                if "0x" in valor:                   # busca valores hexadecimal
                    valor = int(valor,16)
                                
                elif "-" in valor:                  # busca valores negativos
                    valor = int(valor)
                
                elif valor in etiqueta:             # busca etiquetas de brinco
                    valor = n_etiqueta[etiqueta.index(valor)]
                
                elif "x" in valor:                  # busca registros
                    valor = memonicos.registro_decode(valor)
                
                else:                               # hace cast de string a numero
                    valor = int(valor)

            #print("V",contador,"=",valor,end=("; "))
            
            reorder[linea_codigo].append(valor)
            contador += 1

        linea_codigo += 1
    
    #------------------- LEE LOS DATOS DEL ARREGLO Y MANDA A SALIDA --------------------
    if type_out == 1:
        archivo = open("output.txt","a")
    elif type_out == 2:
        archivo = open("output.txt","wb")
    
    for linea in reorder:
        memonicos.write_output(archivo,linea,type_out)

    archivo.close()

    #print(n_etiqueta)
    #print(etiqueta)
    #print(reorder)

    os.system("cat output.txt")
if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
# Main que jala todo

# By: El equipo del cielo
# De Angeles Castillo Isaias & Hernández Vázquez Dafne Angélica

import os
import sys

from convert import convertion

def readFile(nombre_archivo): #Funcion para leer el archivo
    f = open(nombre_archivo, "r") #permisos para leer
    content = f.read().split("\n") # dividir la entrada despues de un salto de linea
    f.close()
    return content

print("Ingrese el nombre de archivo con extensión, ejemplo: codigo2.txt")
nombre_archivo = input("Archivo:  ") 
archivo = readFile(nombre_archivo)

aux = []  #guardar
linenum_tag = [] #va a guardar num de linea donde va un tag
val_tag = []
tags = {}

for j in range(len(archivo)):
    if(":" in archivo[j]):
        val_tag.append(j+1)
        aux.extend(archivo[j].split(":"))
        linenum_tag.append(aux[j])
        del aux[j]
    else:
        aux.extend(archivo[j].split(":"))

for j in range (len(linenum_tag)):
    tags[linenum_tag[j]] = val_tag[j]

print("El archivo generado se llama conversion.txt")

#Guardar en el archivo conversión

orig_stdout = sys.stdout 
file_path = 'conversion.txt'
sys.stdout = open(file_path, "w") #imprime a archivo

for x in range(len(aux)-1):
    archivo[x] = convertion(aux[x]) #pasara por nuestra funcion conversora 
    
sys.stdout.close()
sys.stdout = orig_stdout


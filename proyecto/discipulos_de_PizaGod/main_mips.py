# Converts MIPS instructions into binary and hex
import os
import sys
import argparse #para parsear

from dic_mnemonicos import instr_decode # converts the instruction part of a line of MIPS code
from registerlist import reg_decode # converts the register and immediate parts of the MIPS code

#########
PC=1  #añadido  
ETIQUETAS = [] #añadido
DIR_ETIQUETAS=[] #añadido
##########

def readFile(filen): #Function that reads a file 
    f = open(filen, "r") #read permissions 
    content = f.read().split("\n") #splits input after line jump
    f.close()
    return content

print("Ingrese el nombre de archivo con extensión, ejemplo: codigo2.txt")
archivo = input("Archivo:  ") 
archivo = readFile(archivo)

aux = []  #guardar
linenum_tag = [] #va a guardar num de linea donde va un tag
val_tag = []
tags = {}

for j in range(len(archivo)):
    if(":" in archivo[j]):
        val_tag.append(j+1)
        linenum_tag.extend(archivo[j].split(":"))
        linenum_tag.append(aux[j])
        del aux[j]
    else:
        aux.extend(archivo[j].split(":"))

for j in range (len(linenum_tag)):
    tags[linenum_tag[j]] = val_tag[j]
###
print("El archivo generado se llama conversion.txt")

orig_stdout = sys.stdout #guarda console original

file_path = 'conversion.txt'
sys.stdout = open(file_path, "w") #imprime a archivo


for x in range(len(aux)-1):
    archivo[x] = convertion(aux[x]) #pasara por nuestra funcion conversora 
    
sys.stdout.close() 
sys.stdout = orig_stdout 

# Converts MIPS instructions into binary and hex
import os
import sys

from convert import convertion

def readFile(nombre_archivo): #Function that reads a file 
    f = open(nombre_archivo, "r") #read permissions 
    content = f.read().split("\n") #splits input after line jump
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
###
print("El archivo generado se llama conversion.txt")

orig_stdout = sys.stdout 

file_path = 'conversion.txt'
sys.stdout = open(file_path, "w") #imprime a archivo


for x in range(len(aux)-1):
    archivo[x] = convertion(aux[x]) #pasara por nuestra funcion conversora 

#sys.stdout.close()
#sys.stdout = orig_stdout

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

print("El archivo generado se llama conversion.txt")

orig_stdout = sys.stdout #guarda console original

file_path = 'conversion.txt'
sys.stdout = open(file_path, "w") #imprime a archivo

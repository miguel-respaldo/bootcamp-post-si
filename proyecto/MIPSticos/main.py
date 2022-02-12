#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later


from pickletools import opcodes
import re
import os
import argparse


from diccionarios import mnemonicos_dict_I,mnemonicos_dict_J,registers,funct

labels_list =[]#se almacenarar etiquetas Y dir en mem correspondiente 


def read_assembly(asm_name) :  # retorna una lista con las lineas del archivo sin salto de linea
    with open(asm_name) as f: 
        lines = [re.sub(r"[\n\t]*", "", line) for line in f] # quita el salto de linea 
    return lines 

def identify_labels(file_lines):
    PROGRAM_COUNTER = 4194304 # por cada linea aumeNta 4
    for inst in file_lines:
        inst = inst.split(":") # si encuentra : etiqueta
        if(len(inst)==2):#contiene etiqute
            tupla =(inst[0],PROGRAM_COUNTER)
            labels_list.append(tupla)
        #print(inst)
        PROGRAM_COUNTER = PROGRAM_COUNTER +4
        
    #print(labels_list)


def identify_instr(line): # retornar el tipo de instruccion y su opcode en decimal
    line = line.strip() # quitar los espacios alprincipio y al final
    mnemonic = line.split(" ")
    inst = mnemonic[0] # Se obtiene la instruccion
    if inst in mnemonicos_dict_I.keys():
     
        return("I",mnemonicos_dict_I[inst])
    elif inst in mnemonicos_dict_J.keys():

        return("J",mnemonicos_dict_J[inst])
    else:
        return("R",0)
    
def generate_type_J(line):
    line =line.strip()
    line = line.split(" ")
    opc = mnemonicos_dict_J[line[0]] #obteniendo key
    opc = bin(opc)[2:].zfill(6) # opcode etsitosament
    
    for item in labels_list: #recorrer la lista que contine las etiquetas con la dir
       if line[1] in item:
           value = item[1] # la addres se encuntra en la pos 1 de la tupla           
           value =value >>3 # corriemiento para que coincida la dir
           address =bin(value)[2:].zfill(25)# eliminar prefijo 0b rellenar de 0 para completar
           #print(address)
    
    return opc+address
    
    
def generate_type_I(line): # GENERA TIPOS I
    line=line.strip() # quitar los espacios alprincipio y al final
    
    line = line.split(" ") #se convierte en una lista de 2 elementos 
    
    setInst = identify_instr(line[0]) # tupla coon type y opcode decimal
    
    
    trinity = line[1].split(",")
  
    opc = bin(setInst[1])[2:].zfill(6) # opcode etsitosament
    rs = bin(registers[trinity[0]])[2:].zfill(5)
    rt = bin(registers[trinity[1]])[2:].zfill(5)
    immte = bin(int(trinity[2]))[2:].zfill(16)
    
    return opc+rs+rt+immte

def generate_type_R(line):
    line = line.strip()
    line = line.split(" ")
    setInst = identify_instr(line[0])
    opc = bin(setInst[1])[2:].zfill(6)
    trinity = line[1].split(",")
    rd = bin(registers[trinity[0]])[2:].zfill(5)
    rs = bin(registers[trinity[1]])[2:].zfill(5)
    rt = bin(registers[trinity[2]])[2:].zfill(5)

    shamt = bin(0)[2:].zfill(5)
    fnct = bin(funct["add"])[2:].zfill(6)
    
    return opc+rs+rt+rd+shamt+fnct
    
 
lines_of_file= read_assembly("caliz.asm") # aqui se obtiene el archivo como una lista
identify_labels(lines_of_file)


print(generate_type_J(lines_of_file[13]))


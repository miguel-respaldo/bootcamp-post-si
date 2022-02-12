#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later


import re

import os
import argparse

from diccionarios import mnemonicos_dict_I,mnemonicos_dict_J,registers,funct
labels_list =[]#se almacenarar etiquetas Y dir en mem correspondiente 
PROGRAM_COUNTER = 4194304 # por cada linea aumeNta 4


def read_assembly(asm_name) :  # retorna una lista con las lineas del archivo sin salto de linea
    with open(asm_name) as f: 
        lines = [re.sub(r"[\n\t]*", "", line) for line in f] # quita el salto de linea 
    return lines 

def identify_labels(file_lines):
    PC = 4194304
    cont = 0
    for inst in file_lines:
        inst = inst.split(":") # si encuentra : etiqueta
        if(len(inst)==2):#contiene etiqute
            tupla =(inst[0],PC)
            labels_list.append(tupla)
            file_lines[cont] = file_lines[cont].replace(inst[0]+":","")
            
        cont=cont+1    
        PC = PC +4

    return file_lines    

def identify_instr(line): # retornar el tipo de instruccion y su opcode en decimal
    line=line.strip() # quitar los espacios alprincipio y al final
    line = line.split(",") #se convierte en una lista de 2 elementos 
    inst = line[0] # Se obtiene la instruccion
    if inst in mnemonicos_dict_I.keys():
     
        return("I",mnemonicos_dict_I[inst])
    elif inst in mnemonicos_dict_J.keys():

        return("J",mnemonicos_dict_J[inst])
    else:
        return("R",0)
    
def generate_type_J(line):
    line=line.strip() # quitar los espacios alprincipio y al final
    line = line.split(",") #se convierte en una lista de 2 elementos 
    opc = mnemonicos_dict_J[line[0]] #obteniendo key
    opc = bin(opc)[2:].zfill(6) # opcode etsitosament
    address =bin(0)[2:].zfill(25)
    for item in labels_list: #recorrer la lista que contine las etiquetas con la dir
        if line[1].strip() in item:
            value = item[1] # la addres se encuntra en la pos 1 de la tupla           
            value =value >>3 # corriemiento para que coincida la dir
            address =bin(value)[2:].zfill(26)# eliminar prefijo 0b rellenar de 0 para completar

    return opc+address
     
def generate_type_I(line): # GENERA TIPOS I
    line=line.strip() # quitar los espacios alprincipio y al final
    line = line.split(",") #se convierte en una lista de 2 elementos 
    setInst = identify_instr(line[0]) # tupla coon type y opcode decimal
    
    opc = bin(setInst[1])[2:].zfill(6) # opcode etsitosament
    immte=bin(0).zfill(16)

    if(setInst[1] == 4 or setInst[1] == 5): # en caso que sea un branch
        for item in labels_list: #recorrer la lista que contine las etiquetas con la dir
            
            if line[3].strip() in item:
                value = item[1] # la addres se encuntra en la pos 1 de la tupla
                value = value-17 #  PC=PC+4+BranchAddr invertido   
                  
                #value =value >>3 # corriemiento para que coincida la dir
                immte =bin(value)[2:].zfill(16)# eliminar prefijo 0b rellenar de 0 para completar
                immte = immte[6:]
        rs = bin(registers[line[2].strip()])[2:].zfill(5)
    elif line[3] in registers.keys():
        value = registers[line[3]]
        immte =bin(value)[2:].zfill(16)# eliminar prefijo 0b rellenar de 0 para completar  
        
        rs = bin(int(line[2].strip()))[2:].zfill(5)        
    else:        
        value = eval(line[3]) #eval porque puede venir en exa
                    #chorote adentro para cuando son valores negativos
        immte = bin(value if value>=0 else value+(1<<16))[2:].zfill(16)
        rs = bin(registers[line[2].strip()])[2:].zfill(5) 


    rt = bin(registers[line[1].strip()])[2:].zfill(5)
    #rs = bin(registers[line[2].strip()])[2:].zfill(5)
    immte = immte[len(immte)-16:]
    return opc+rs+rt+immte

def generate_type_R(line):
    line=line.strip() # quitar los espacios alprincipio y al final
    line = line.split(",") #se convierte en una lista de 2 elementos 
    setInst = identify_instr(line[0])
    opc = bin(setInst[1])[2:].zfill(6)
    
    rd = bin(registers[line[1].strip()])[2:].zfill(5)
    rs = bin(registers[line[2].strip()])[2:].zfill(5)
    rt = bin(registers[line[3].strip()])[2:].zfill(5)
  
    shamt = bin(0)[2:].zfill(5)
    fnct = bin(funct[line[0]])[2:].zfill(6)
    
    return opc+rs+rt+rd+shamt+fnct
    
def generate_bin_txt(lines_of_file,nombre_de_salida):
    with open(nombre_de_salida,"w") as f:
        binary_inst = "0"
        for line in lines_of_file:
            inst_type = identify_instr(line)
            if inst_type[0] == "I":
                binary_inst= generate_type_I(line)
            elif inst_type[0] == "R":
                binary_inst = generate_type_R(line)
            elif inst_type[0] == "J":
                binary_inst=generate_type_J(line)

            #print(binary_inst)
            f.write(binary_inst+"\n")

def generate_hex_bin(filename):
    binary_lines = []
    hex_lines=[]
    with open(filename) as f: # guardando todo el txt en una lista de cadena sin salto de linea
        for line in f:
            binary_lines.append(line.strip("\n"))
    
    binFile= open(filename+"-BINARY","wb")

    #print(binascii.unhexlify("ff"))
    baits = bytearray(4)
    for line in binary_lines:
        div_line =[]
        div_line.append(int(line[0:8],2))
        div_line.append(int(line[8:16],2))
        div_line.append(int(line[16:24],2))
        div_line.append(int(line[24:32],2))

        baits[0]= div_line[3]
        baits[1]= div_line[2]
        baits[2]= div_line[1]
        baits[3]= div_line[0]
        
        binFile.write(baits)
        
        hex_lines.append((div_line))
   
    binFile.close()

def main():
    """
    Función principal del programa
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("archivo", help="Archivo de entrada")
    parser.add_argument("-t", "--text",
                        action="store", dest="nombre_de_salida", default="salida.o",
                        help="Nombre de archivo de salida")
    parser.add_argument("-o", "--output",
                        action="store", dest="nombre_de_salida", default="salida.o",
                        help="Nombre de archivo de salida")

    args = parser.parse_args()
    
    if not os.path.exists(args.archivo):
        print(f"No se encuentra el archivo {args.archivo}")
        exit(1)

    lines_of_file= read_assembly(args.archivo) # aqui se obtiene el archivo como una lista
    lines_of_file=identify_labels(lines_of_file) # se actualiza la lista de lineas pero con las etiquetas almacenadas en otra locacion
    
    generate_bin_txt(lines_of_file,args.nombre_de_salida) # genera el archivo txt binario
    generate_hex_bin(args.nombre_de_salida)

    print("Archivo:",args.archivo)
    print("Salida txt:",args.nombre_de_salida)
    print("Salida bin:",args.nombre_de_salida,"-BINARY")


main()





 
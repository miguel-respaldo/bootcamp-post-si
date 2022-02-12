#conversion_module
#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

from dic_mnemonicos import instr_decode  #converts instruction part of a line code (MIPS)
from dic_register import reg_decode #converts register & immediate parts of a line code (MIPS)

def convertion(code_instruction):
    code_instruction = "".join(code_instruction.split()) #elimina todos los espacios en blanco, tab, \n
    code_instruction = code_instruction.replace(",", " ") 
    code_instruction = code_instruction.replace(":", " ")
 
    args = code_instruction.split(" ") #despues de cada espacio divide los argumentos
    instruction = args[0] #posicion en 0 para la instrucion (codigo)
   
    codes = instr_decode(instruction) #colocamos el valor de opcode a codes
    func_type = codes[0]   #Asignamos a function type el valor anterior para estar en la pos correcta (de acuerdo a los casos)
    reg_values = reg_decode(func_type, instruction, args[1:]) #obtenemos los valores numericos de los registros
     
   #por diferentes tipos, r, i, b, j
    if func_type == "r":            
        opcode = '{0:04b}'.format(codes[1])
        rs = '{0:03b}'.format(reg_values[0])
        rt = '{0:03b}'.format(reg_values[1])
        rd = '{0:03b}'.format(reg_values[2])
        filler = '{0:05b}'.format(reg_values[3])
        b = opcode+rs+rt+rd+filler
        print(b)
        
    elif func_type == "i":
        opcode = '{0:04b}'.format(codes[1])
        rs = '{0:03b}'.format(reg_values[0])
        rt = '{0:03b}'.format(reg_values[1])
        if reg_values[2] < 0:
            imm = (bin(((1 << 8) -1) & reg_values[2])[2:]).zfill(8)
        else:
            imm = '{0:08b}'.format(reg_values[2]) 
        b = opcode+rs+rt+imm
        print(b)
    
    elif func_type == "b":
        opcode = '{0:04b}'.format(codes[1])
        rs = '{0:03b}'.format(reg_values[0])
        rt = '{0:03b}'.format(reg_values[1])
        label = '{0:08b}'.format(reg_values[2])
        b = opcode+rs+rt+label
        print(b)

    elif func_type == "j":
        opcode = '{0:04b}'.format(codes[1])
        imm = '{0:014b}'.format(reg_values[0])
        b = opcode+imm
        print(b)
        
    else:
        print("Interpretation Error") #Error de interpretacion
        return 
           
    return

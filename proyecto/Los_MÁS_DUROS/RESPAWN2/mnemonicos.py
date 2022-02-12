#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

def i_decodificado(instruc):
    if instruc == "add":    #Instrucción ADD tipo R
        tipo = "r"
        opcode = 0
        
    elif instruc == "addi": #Instrucción ADDI tipo I
        tipo = "i"
        opcode = 0x1
    
    elif instruc == "and":  #Instrucción AND tipo R
        tipo = "r"
        opcode = 0x2

    elif instruc == "andi": #Instrucción ANDI tipo I
        tipo = "i"
        opcode = 0x3
        
    elif instruc == "beq":  #Instrucción BEQ tipo B
        tipo = "b"          #(es tipo I)
        opcode = 0x4
        
    elif instruc == "bne":  #Instrucción BNE tipo B
        tipo = "b"          #(es tipo I)
        opcode = 0x5
        
    elif instruc == "j":    #Instrucción JUMP tipo J
        tipo = "j"
        opcode = 0x6
           
    elif instruc == "jal":  #Instrucción JAL tipo J
        tipo = "j"
        opcode = 0x7
    
    elif instruc == "jr":   #Instrucción JR tipo J
        tipo = "r"
        opcode = 0xa
     
    elif instruc == "lb":   #Instrucción LB tipo I
        tipo = "i"
        opcode = 0xb
        
    elif instruc == "or":   #Instrucción OR tipo R
        tipo = "r"
        opcode = 0xc
        
    elif instruc == "sb":   #Instrucción SB tipo I
        tipo = "i"
        opcode = 0xd
        
    elif instruc == "sll":  #Instrucción SLL tipo R
        tipo = "r"
        opcode = 0xe
    
    elif instr == "srl":    #Instrucción SRL tipo R
        tipo = "r"
        opcode = 0xf
        
    else:
        tipo = None
        opcode = None
    
    return [tipo, opcode]

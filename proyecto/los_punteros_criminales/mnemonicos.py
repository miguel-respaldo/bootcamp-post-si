#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later



def instr_decode(instr):
    if instr == "add":
        func_type = "r"
        opcode = 0
        
    elif instr == "addi":
        func_type = "i"
        opcode = 0x1
    
    elif instr == "and":
        func_type = "r"
        opcode = 2

    elif instr == "andi":
        func_type = "i"
        opcode = 0x3
        
    elif instr == "beq":
        func_type = "b"
        opcode = 0x4
        
    elif instr == "bne":
        func_type = "b"
        opcode = 0x5
        
    elif instr == "j":
        func_type = "j"
        opcode = 0x6
           
    elif instr == "jal":
        func_type = "j"
        opcode = 0x7
    
    elif instr == "jr":
        func_type = "r"
        opcode = 0xa
     
    elif instr == "lb":
        func_type = "i"
        opcode = 0xb
        
    elif instr == "or":
        func_type = "r"
        opcode = 0xc
        
    elif instr == "sb":
        func_type = "i"
        opcode = 0xd
        
    elif instr == "sll":
        func_type = "r"
        opcode = 0xe
    
    elif instr == "srl":
        func_type = "r"
        opcode = 0xf
        
    else:
        func_type = None
        opcode = None
    
    return [func_type, opcode]

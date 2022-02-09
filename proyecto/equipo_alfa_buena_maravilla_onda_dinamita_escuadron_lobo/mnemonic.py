#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
MNEMONIC

"""

#####Aqui se definen los Mnemonicos####

def mnemonicos(mnemonic):
    if mnemonic=="add":
        op=0x0
        tipo_instruccion="r"
    
    elif mnemonic=="addi":
        op=0x1
        tipo_instruccion="i" 
    
    elif mnemonic=="and":
        op=0x2
        tipo_instruccion="r"
    
    elif mnemonic=="andi":
        op=0x3
        tipo_instruccion="i"

    elif mnemonic=="beq":
        op=0x4
        tipo_instruccion="i"
        
    elif mnemonic=="bne":
        op=0x5
        tipo_instruccion="i"
    
    elif mnemonic=="j":
        op=0x6
        tipo_instruccion="j"
    
    elif mnemonic=="jal":
        op=0x7
        tipo_instruccion="j"

    elif mnemonic=="jr":
        op=0xa
        tipo_instruccion="r"

    elif mnemonic=="lb":
        op=0xb
        tipo_instruccion="i"

    elif mnemonic=="or":
        op=0xc
        tipo_instruccion="r"

    elif mnemonic=="sb":
        op=0xd
        tipo_instruccion="i"

    elif mnemonic=="sll":
        op=0xe
        tipo_instruccion="r"

    elif mnemonic=="srl":
        op=0xf
        tipo_instruccion="r"

    else:
        op=None
        tipo_instruccion=None
    
    return(op,tipo_instruccion)


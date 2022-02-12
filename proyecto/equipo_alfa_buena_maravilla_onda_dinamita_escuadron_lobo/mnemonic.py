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
        op=0
        #tipo_instruccion="r"
    
    elif mnemonic=="addi":
        op=1
        #tipo_instruccion="i" 
    
    elif mnemonic=="and":
        op=2
        #tipo_instruccion="r"
    
    elif mnemonic=="andi":
        op=3
        #tipo_instruccion="i"

    elif mnemonic=="beq":
        op=4
        #tipo_instruccion="i"
        
    elif mnemonic=="bne":
        op=5
        #tipo_instruccion="i"
    
    elif mnemonic=="j":
        op=6
        #tipo_instruccion="j"
    
    elif mnemonic=="jal":
        op=7
        #tipo_instruccion="j"

    elif mnemonic=="jr":
        op=10
        #tipo_instruccion="r"

    elif mnemonic=="lb":
        op=11
        #tipo_instruccion="i"

    elif mnemonic=="or":
        op=12
        #tipo_instruccion="r"

    elif mnemonic=="sb":
        op=13
        #tipo_instruccion="i"

    elif mnemonic=="sll":
        op=14
        #tipo_instruccion="r"

    elif mnemonic=="srl":
        op=15
        #tipo_instruccion="r"

    else:
        op=None
        #tipo_instruccion=None
    
    return(op)


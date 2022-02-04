#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

from mnemonicos import mnemonicos_dict

def read_assembly(asm_name) -> list:  # retorna una lista con las lineas del archivo sin salto de linea
    with open(asm_name) as f: 
        lines = [line.rstrip('\n') for line in f] # quita el salto de linea    
    return lines 

def identify_instr(line):
    mnemonic = line.split(" ")
    return mnemonic[0]

    
    

    
lines_of_file= read_assembly("caliz.asm")
caliz = identify_instr(lines_of_file[0])
print(mnemonicos_dict[caliz])
print(lines_of_file[0])

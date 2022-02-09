#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

tipo_instrucciones={
    "add" : ["r",0x0],
    "addi": ["i",0x1],
    "and":  ["r",0x2],
    "andi": ["i",0x3],
    "beq":  ["b",0x4],
    "bne":  ["b",0x5],
    "j":    ["j",0x6],
    "jal":  ["j",0x7],
    "jr":   ["r",0xa],
    "lb":   ["i",0xb],
    "or":   ["r",0xc],
    "sb":   ["i",0xd],
    "sll":  ["r",0xe],
    "srl":  ["r",0xf]
}

def instr_decode(instr):
    func_type=tipo_instrucciones[instr][0]
    opcode=tipo_instrucciones[instr][1]
    return [func_type, opcode]

def instr_decode(instr):
    tipoR = {'add' : 0 , 'and' : 2, 'jr' : 0xa, 'or' : 0xc, 'sll' : 0xe, 'srl' : 0xf }
    tipoI = {'addi' : 0x1 , 'andi' : 0x3, 'lb' : 0xb, 'sb' : 0xd }
    tipoB = {'beq' : 0x4 , 'bne' : 0x5 } #Tipo Branch
    tipoJ = {'j' : 0x6 , 'jal' : 0x7 }

    if instr in tipoR:
        opcode = tipoR[instr]
        func_type = "r"
    elif instr in tipoI:
        opcode = tipoI[instr]
        func_type = "i"
    elif instr in tipoB:
        opcode = tipoB[instr]
        func_type = "b"
    elif instr in tipoJ:
        opcode = tipoJ[instr]
        func_type = "j"
    else:
        func_type = None
        opcode = None

    return [func_type, opcode]

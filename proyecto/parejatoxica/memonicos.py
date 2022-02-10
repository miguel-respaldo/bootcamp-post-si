
def instruction_decode(instruccion):
    tipoR = {'add' : 0 , 'and' : 2, 'jr' : 0xa, 'or' : 0xc, 'sll' : 0xe, 'srl' : 0xf } #Tipo R 
    tipoI = {'addi' : 0x1 , 'andi' : 0x3, 'lb' : 0xb, 'sb' : 0xd } #Tipo I
    tipoB = {'beq' : 0x4 , 'bne' : 0x5 } #Tipo Branch
    tipoJ = {'j' : 0x6 , 'jal' : 0x7 } #Tipo J
    
    #print("Se recibe la instruccion:",instruccion)

    if instruccion in tipoR:
        opcode = tipoR[instruccion]
        func_type = "r"

    elif instruccion in tipoI:
        opcode = tipoI[instruccion]
        func_type = "i"

    elif instruccion in tipoB:
        opcode = tipoB[instruccion]
        func_type = "b"

    elif instruccion in tipoJ:
        opcode = tipoJ[instruccion]
        func_type = "j"

    else:
        opcode = None
        func_type = None

    return [func_type, opcode]


def write_output(tipo,val):
    
    print("\n")
    #print(tipo,end="; ")
    #print(val,end="; ")
    #print(eti,end="; ")




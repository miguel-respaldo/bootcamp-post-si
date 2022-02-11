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


def registro_decode(registro):
    reg = {'x0':0, 'x1':1, 'x2':2, 'x3':3, 'x4':4, 'x5':5, 'x6':6, 'x7':7, 'x8':8, 'x9':9}
    
    if registro in reg:
        val_reg = reg[registro]
    else:
        val_reg = registro
    
    return val_reg


def write_output(salida,val):

    #print(val[0][0])
    
    if val[0][0] == "r":
        #print("Instruccion tipo R")
        
        opcode = '{0:06b}'.format(0)
        
        salida.write(opcode)
        
        #None

    if val[0][0] == "r":
        #print("Instruccion tipo R")

        None
    
    if val[0][0] == "r":
        #print("Instruccion tipo R")

        None

    if val[0][0] == "r":
        #print("Instruccion tipo R")
        
        None



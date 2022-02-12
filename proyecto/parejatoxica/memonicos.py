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


def write_output(output,val,tipo):

    print(val)
    out = ""                                    # variable para reordenar y guardar en bits
    baits = bytearray(4)                        # variable para salida en bytes

    if val[0][0] == "r":                        # formatea las instrucciones R
        #print("Instruccion tipo R")
        
        shamt = 0
        if (val[0][1] == 14 or (val[0][1] == 15)):  # checa si la instruccion es sll o srl
            shamt = val[3]
            
            opcode = '{0:06b}'.format(0)
            rd = '{0:05b}'.format(val[1])
            rs = '{0:05b}'.format(val[2])
            rt = '{0:05b}'.format(val[3])
            shamt = '{0:05b}'.format(shamt)
            funct = '{0:06b}'.format(val[0][1])

        elif val[0][1] == 10:                   # checa si la instruccion es jr
            opcode = '{0:06b}'.format(0)
            rd = '{0:05b}'.format(0)
            rs = '{0:05b}'.format(val[1])
            rt = '{0:05b}'.format(0)
            shamt = '{0:05b}'.format(0)
            funct = '{0:06b}'.format(val[0][1])
        
        else:                                   # cualquier otra instruccion tipo R
            opcode = '{0:06b}'.format(0)
            rd = '{0:05b}'.format(val[1])
            rs = '{0:05b}'.format(val[2])
            rt = '{0:05b}'.format(val[3])
            shamt = '{0:05b}'.format(0)
            funct = '{0:06b}'.format(val[0][1])

        out = opcode + rs + rt + rd + shamt + funct
        #None

    elif val[0][0] == "i":                      # formatea las instrucciones I
        #print("Instruccion tipo I")
        
        if val[3] < 0:                          # checa si immediate es negativo
           val[3] &= 0xFFFF
        
        opcode = '{0:06b}'.format(val[0][1])
        rt = '{0:05b}'.format(val[1])
        rs = '{0:05b}'.format(val[2])
        immediate = '{0:016b}'.format(val[3])
        
        out = opcode + rs + rt + immediate
        None
    
    elif val[0][0] == "b":                      # formatea las instrucciones B
        #print("Instruccion tipo R")
        
        opcode = '{0:06b}'.format(val[0][1])
        rt = '{0:05b}'.format(val[1])
        rs = '{0:05b}'.format(val[2])
        offset = '{0:016b}'.format(val[3])

        out = opcode + rs + rt + offset
        #None

    elif val[0][0] == "j":                      # formatea las instrucciones J
        #print("Instruccion tipo R")
        
        opcode = '{0:06b}'.format(val[0][1])
        target = '{0:026b}'.format(val[1])
        
        out = opcode + target
        #None   

    # Se separa el binario por bytes y guarda en variable
    baits[0] = int(out[0:8],2)
    baits[1] = int(out[8:16],2)
    baits[2] = int(out[16:24],2)
    baits[3] = int(out[24:33],2)
    
    # Escribe en archivo dependiendo del tipo de salida
    if tipo == 1:
        output.write(out)
        output.write("\n")
    elif tipo == 2:
        output.write(baits)


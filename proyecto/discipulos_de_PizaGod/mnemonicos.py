def instr_decode(instr):
    tipoR = {'add' : 0 , 'and' : 2, 'jr' : 0xa, 'or' : 0xc, 'sll' : 0xe, 'slr' : 0xf }
    tipoI = {'addi' : 0x1 , 'andi' : 0x3, 'lb' : 0xb, 'sb' : 0xd }
#Definiendo instrucciones basicas para nuestra deteccion de instrucciones   


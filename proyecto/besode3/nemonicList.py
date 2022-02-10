# Diccionario que contiene el "funct" de cada instruccion de las tipo R
rType = {
    'add' : 0b0000,
    'and' : 0b0010,
    'jr'  : 0b1010,
    'sll' : 0b1110,
    'srl' : 0b1111,
    'or'  : 0b1100,
    'jr' :  0b1010
}

# Diccionario que contiene el "opcode" de cada instruccion de las tipo I
iType = {
    "addi" : 0b0001,
    "andi" : 0b0011,
    "beq"  : 0b0100,
    "bne"  : 0b0101,
    "lb"   : 0b1011,
    'sb'   : 0b1101
}

# Diccionario que contiene el "opcode" de cada instruccion de las tipo J
jType = {
    "j"     : 0b0110,
    "jal"   : 0b0111
}
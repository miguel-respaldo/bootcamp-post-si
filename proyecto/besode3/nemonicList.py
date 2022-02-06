# Diccionario que contiene el "funct" de cada instruccion de las tipo R
rType = {
    "add"   : 0b100000,
    "addu"  : 0b100001,
    "and"   : 0b100100,
    "jr"    : 0b001000,
    "nor"   : 0b100111,
    "or"    : 0b100101,
    "slt"   : 0b101010,
    "sltu"  : 0b101011,
    "sll"   : 0b000000,
    "sllv"  : 0b000100,
    "srl"   : 0b000010,
    "sub"   : 0b100010,
    "subu"  : 0b100011,
    "mfhi"  : 0b010000,
    "mflo"  : 0b010010,
    "mult"  : 0b011000,
    "multu" : 0b011001,
    "sra"   : 0b000011,
    "xor"   : 0b100110
}

# Diccionario que contiene el "opcode" de cada instruccion de las tipo I
iType = {
    "addi"  : 0b001000,
    "addiu" : 0b001001,
    "andi"  : 0b001100,
    "beq"   : 0b000100,
    "bne"   : 0b000101,
    "lb"    : 0b100000,
    "lbu"   : 0b100101,
    "lh"    : 0b100001,
    "lui"   : 0b001111,
    "lw"    : 0b100011,
    "ori"   : 0b001101,
    "slti"  : 0b001010,
    "sltiu" : 0b001011,
    "sb"    : 0b101000,
    "sh"    : 0b101001,
    "sw"    : 0b101011,
    "xori"  : 0b001110
}

# Diccionario que contiene el "opcode" de cada instruccion de las tipo J
jType = {
    "j"     : 0b000010,
    "jal"   : 0b000011
}
from nemonicList import *

# Si un nemonico pertenece a algun tipo, retorna el tipo al que pertencece 
def getType(nemonic):
    if nemonic in rType: return 'R'
    if nemonic in iType: return 'I'
    if nemonic in jType: return 'J'
    return None

# R[rd] = R[rs] + R[rt]
def instructionR(nemonic, rd, rs, rt):
    out = 0
    op = 0b000000
    funct = rType[nemonic]
    
    out = out << 6
    out += op
    out = out << 5
    out += rs
    out = out << 5
    out += rt
    out = out << 5
    out += rd
    out = out << 5
    out += 0b00000
    out = out << 6
    out += funct

    return out

# R[rt] = R[rs] + Imm
def instructionI(nemonic, rt, rs, imm):
    out = 0
    op = iType[nemonic]

    out += op
    out = out << 5
    out += rs
    out = out << 5
    out += rt
    out = out << 16
    out += imm

    return out

def instructionJ(nemonic, address):
    out = 0
    op = jType[nemonic]
    address = address >> 2

    out += op
    out = out << 26
    out += address
    
    return out
from nemonicList import *

class input:
    def __init__(self,instruction, tag, nemonic, rs, rt, rd, imm, address, pc, tipo, machineCode):
        self.instruction = instruction
        self.tag = tag
        self.nemonic = nemonic
        self.rs = rs
        self.rt = rt
        self.rd = rd
        self.imm = imm
        self.address = address
        self.pc = pc
        self.tipo = tipo
        self.machineCode = machineCode
    
    def imprimir(self):
        if getType(self.nemonic) == 'R': 
            if self.nemonic == 'jr':
                print(self.tag, self.nemonic, self.rs, "\t", f"{self.pc}", end="\t")
            else:
                print(self.tag, self.nemonic, self.rs, self.rt, self.rd, "\t", f"{self.pc}", end="\t")
        
        if getType(self.nemonic) == 'I': 
            print(self.tag, self.nemonic, self.rt, self.rs, self.imm, "\t", f"{self.pc}", end="\t")

        if getType(self.nemonic) == 'J': 
            print(self.tag, self.nemonic, f"{self.address:#x}", "\t", f"{self.pc}", end="\t")
        
        #print(self.tag, self.nemonic, self.rs, self.rt, self.imm, f"{self.address:#x}","\t", f"{self.pc:#x}", end="\t")

        print(f"{self.machineCode:018b}")
        

# Si un nemonico pertenece a algun tipo, retorna el tipo al que pertencece
def getType(nemonic):
    if nemonic in rType: return 'R'
    if nemonic in iType: return 'I'
    if nemonic in jType: return 'J'
    return None

# R[rd] = R[rs] + R[rt]
def instructionR(nemonic, rs, rt, rd):
    out = 0
    op = 0b0000
    op = rType[nemonic]
    
    out = out << 4
    out += op
    out = out << 3
    out += rs
    out = out << 3
    out += rt
    out = out << 3
    out += rd
    out = out << 5
    out += 0b00000

    return out

# R[rt] = R[rs] + Imm
def instructionI(nemonic, rt, rs, imm):
    out = 0
    op = iType[nemonic]

    out += op
    out = out << 3
    out += rs
    out = out << 3
    out += rt
    out = out << 8
    if imm < 0: out += imm + (1 << 8)
    else: out += imm
    
    return out

def instructionJ(nemonic, address):
    out = 0
    op = jType[nemonic]
    out += op
    out = out << 14
    out += address
    
    return out
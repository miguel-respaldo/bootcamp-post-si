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
    else: 'X'
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

def convertArgumentsR(nemonic, args):
    
    if nemonic == "jr":
        # Las instrucciones "jr" solo usan rs
        rs = int(args[0][1: ])
        rt, rd = 0, 0
    elif nemonic == 'sll' or nemonic == 'srl':
        # Solo instrucciones 'sll' y 'slr' cambia el orden de los argumentos de 'rs, rt, rd'
        rd = int(args[0][1: ])
        rt = int(args[1][1: ])
        rs = int(args[2][1: ])
    else:
        # Para el resto de las instrucciones
        rd = int(args[0][1: ])
        rs = int(args[1][1: ])
        rt = int(args[2][1: ])
    
    return rs, rt, rd

def convertArgumentsI(nemonic, args):
    # Convertir en numeros los args
    for i in range(len(args)):
        if args[i].isnumeric(): # Para numeros positivos
            args[i] = int(args[i]) 
        elif args[i].startswith('-') and args[i][1:].isnumeric(): # Para numeros negativos
            args[i] = int(args[i][1:]) 
            args[i] *= -1
            args[i] = args[i] + (1 << 8)
        elif args[i].startswith('x'): # Para numeros los registros
            args[i] = int(args[i][1 :])
        elif args[i].startswith('0x'): # Para numeros hexadecimales
            args[i] = int(args[i], 16)
        elif args[i].startswith('0b'): # Para numeros binarios
            args[i] = int(args[i], 2)
    
    if nemonic != 'beq' and nemonic != 'bne':
        # Para cualquier otra que no sea 'beq' y 'bne'
        rt = args[0]
        rs = args[1]
        imm = args[2]
        
        #codigoMaquina = instructionI(nemonico, rt, rs, imm)
    
    if nemonic == 'lb' or nemonic == 'sb':
        # 'lb' y 'sb' tiene un orden distinto al guardar los args
        rt = args[0]
        imm = args[1]
        rs = args[2]
        
        #codigoMaquina = instructionI(nemonico, rt, rs, imm)
    else:
        # Aqui van  a entrar las instrucciones 'beq' y 'bne' 
        # pero no se genera codigo maquina para generarlo despues cuando encuentre a donde salta
        rt = args[0]
        rs = args[1]
        imm = args[2]

    return rt, rs, imm

def findJumps(inputList):
    # Las funciones de salto como 'j', 'jal', 'beq' y 'bnq' necesitan saber a que linea saltar
    # buscará la instruccion con la etiquta a donde salta para igualar el PC a donde debe saltar
    for i in inputList:
        if i.address != None:
            for j in inputList:
                if i.address == j.tag: 
                    # Aquí solo entran las instrucciones de tipo J
                    i.address = j.pc
                    i.machineCode = instructionJ(i.nemonic, i.address)
                    break
                    

                
                if i.imm == j.tag: 
                    # Aqui entran los bne y beq
                    i.imm = j.pc - i.pc
                    i.machineCode = instructionI(i.nemonic, i.rs, i.rt, i.imm)
                    break
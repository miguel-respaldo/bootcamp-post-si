# the main conversion function
from dic_mnemonicos import instr_decode # converts the instruction part of a line of MIPS code
from dic_register import reg_decode # converts the register and immediate parts of the MIPS code

def convertion(instr):
    instr = instr.replace(" ", "")
    instr = instr.replace(",", " ") 
    instr = instr.replace("  ", " ") 
    instr = instr.replace("   ", "") 
    instr = instr.replace(":", " ") 
    args = instr.split(" ") #dividir despues de cada espacio
    instruction = args[0]
    codes = instr_decode(instruction) 
    func_type = codes[0]   
    reg_values = reg_decode(func_type, instruction, args[1:]) 
 
    if func_type == "r":            
        opcode = '{0:04b}'.format(codes[1])
        rs = '{0:03b}'.format(reg_values[0])
        rt = '{0:03b}'.format(reg_values[1])
        rd = '{0:03b}'.format(reg_values[2])
        filler = '{0:05b}'.format(reg_values[3])
        b = opcode+rs+rt+rd+filler # b = binary 
        print(b)
        
    elif func_type == "i":
        opcode = '{0:04b}'.format(codes[1])
        rs = '{0:03b}'.format(reg_values[0])
        rt = '{0:03b}'.format(reg_values[1])
        if reg_values[2] < 0:
            imm = (bin(((1 << 8) -1) & reg_values[2])[2:]).zfill(8)
        else:
            imm = '{0:08b}'.format(reg_values[2]) 
        b = opcode+rs+rt+imm
        print(b)
    
    elif func_type == "b":
        opcode = '{0:04b}'.format(codes[1])
        rs = '{0:03b}'.format(reg_values[0])
        rt = '{0:03b}'.format(reg_values[1])
        label = '{0:08b}'.format(reg_values[2])
        b = opcode+rs+rt+label #binary
        print(b)
    
    elif func_type == "j":
        opcode = '{0:04b}'.format(codes[1])
        imm = '{0:014b}'.format(reg_values[0])
        b = opcode+imm
        print(b)
    else:
        print("Interpretation Error") #Error de interpretacion 
        return 

    return

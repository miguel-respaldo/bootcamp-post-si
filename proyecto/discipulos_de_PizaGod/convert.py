# the main conversion function
from dic_mnemonicos import instr_decode # converts the instruction part of a line of MIPS code
from dic_register import reg_decode # converts the register and immediate parts of the MIPS code

def converting(instr):
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
 
    #execution for b-type functions
    if func_type == "b":
        opcode = '{0:04b}'.format(codes[1])
        rs = '{0:03b}'.format(reg_values[0])
        rt = '{0:03b}'.format(reg_values[1])
        label = '{0:08b}'.format(reg_values[2])
        b = opcode+rs+rt+label #binary
        print(b)

#conversion_function
from dic_mnemonicos import instr_decode # converts the instruction part of a line of MIPS code
from dic_register import reg_decode # converts the register and immediate parts of the MIPS code

def convertion(code_instruction):
    code_instruction = code_instruction.replace(" ", "")
    code_instruction = code_instruction.replace(",", " ") 
    code_instruction = code_instruction.replace("  ", " ") 
    code_instruction = code_instruction.replace("	", "") 
    code_instruction = code_instruction.replace(":", " ") 
    args = code_instruction.split(" ") #splits the arguments after every espace
    instruction = args[0] #instrucion code is stored in pos 0 
    
    codes = instr_decode(instruction) #Assigns the value of  the opcode
    func_type = codes[0]   #Assigns a function type to be printed according to cases
    reg_values = reg_decode(func_type, instruction, args[1:]) #get the numeric values of the registers
    
    #if reg_values == None:
    #    #print("Not a valid MIPS statement")
    #    print(":( Me declaro incompetente para este caso")
    #    return
     
   #por diferentes tipos, r, i, b, j
    if func_type == "r":            
        opcode = '{0:04b}'.format(codes[1])
        rs = '{0:03b}'.format(reg_values[0])
        rt = '{0:03b}'.format(reg_values[1])
        rd = '{0:03b}'.format(reg_values[2])
        filler = '{0:05b}'.format(reg_values[3])
        b = opcode+rs+rt+rd+filler
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
        b = opcode+rs+rt+label
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

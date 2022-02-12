# the main conversion function
from dic_mnemonicos import instr_decode # converts the instruction part of a line of MIPS code
from dic_register import reg_decode # converts the register and immediate parts of the MIPS code

def converting(code):
    code = code.replace(" ", "")
    args = code.split(" ") #dividir despues de cada espacio
    instruction = args[0]

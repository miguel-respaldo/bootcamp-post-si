import sys
from mnemonicos import instr_decode 
from registerlist import reg_decode 
import os
import argparse

def readFile(fileName):
    fileObj = open(fileName, "r") 
    words = fileObj.read().split("\n") 
    fileObj.close() 
    return words 

def convertir(code):
    code = code.replace(" ", "")
    code = code.replace(",", " ") 
    code = code.replace("  ", " ") 
    code = code.replace("	", "") 
    code = code.replace(":", " ") 
    args = code.split(" ") 
    instruction = args[0]
   
  
    codes = instr_decode(instruction) 
    func_type = codes[0]   
    reg_values = reg_decode(func_type, instruction, args[1:]) 
    
    
    if reg_values == None:
        print("No se puede traducir este rollo")
        return
     
    if func_type == "r":            
        opcode = '{0:04b}'.format(codes[1])
        rs = '{0:03b}'.format(reg_values[0])
        rt = '{0:03b}'.format(reg_values[1])
        rd = '{0:03b}'.format(reg_values[2])
        filler = '{0:05b}'.format(reg_values[3])
        binary = opcode+rs+rt+rd+filler
        print(binary)
        
    
    elif func_type == "b":
        opcode = '{0:04b}'.format(codes[1])
        rs = '{0:03b}'.format(reg_values[0])
        rt = '{0:03b}'.format(reg_values[1])
        label = '{0:08b}'.format(reg_values[2])
        binary = opcode+rs+rt+label
        print(binary)
   
    elif func_type == "i":
        opcode = '{0:04b}'.format(codes[1])
        rs = '{0:03b}'.format(reg_values[0])
        rt = '{0:03b}'.format(reg_values[1])
        if reg_values[2] < 0:
            imm = (bin(((1 << 8) -1) & reg_values[2])[2:]).zfill(8)
        else:
            imm = '{0:08b}'.format(reg_values[2]) 
        binary = opcode+rs+rt+imm
        print(binary)
    
      
    elif func_type == "j":
        opcode = '{0:04b}'.format(codes[1])
        imm = '{0:014b}'.format(reg_values[0])
        binary = opcode+imm
        print(binary)
        
    else:
        print("Its impossible to enter to this print")
        print("If you read this you broke our program")
        return 
           
    return


def main():
	os.system("clear")
	parser = argparse.ArgumentParser()
	parser.add_argument("archivo", help="Archivo de entrada")
	args = parser.parse_args()
	
	if not os.path.exists(args.archivo):
        	print(f"No se encuentra el archivo {args.archivo}")
        	exit(1)
        
	file1 = readFile(args.archivo)
	arguments = []
	codigo = [] 
	codigo2 = [] 
	val_tag = []
	tags = {}
	

	for j in range(len(file1)):
		if(":" in file1[j]):
			val_tag.append(j+1)
			codigo.extend(file1[j].split(":"))
			codigo2.append(codigo[j])
			del codigo[j]
		else:
			codigo.extend(file1[j].split(":"))

	for j in range (len(codigo2)):
		tags[codigo2[j]] = val_tag[j]	

	orig_stdout = sys.stdout 

	file_path = 'output.txt'
	sys.stdout = open(file_path, "w") 


	for x in range(len(codigo)-1):
	    file1[x] = convertir(codigo[x])

	sys.stdout.close()
	sys.stdout = orig_stdout 


if __name__ == "__main__":
    main()

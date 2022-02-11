#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
	Binary Code Generator
"""

import os


class lacoordenada():
	file_name = "codigo2.txt"
	opcodes_dic = {	"R":{"add":"0000", "and":"0010", "jr":"1010", "or":"1100", "sll":"1110", "srl":"1111"}, 
					"J":{"j":"0110", "jal":"0111"}, 
					"I":{"addi":"0001", "andi":"0011", "beq":"0100", "bne":"0101", "lb":"1011", "sb":"1110"} }
	tags_dict = {}
	listinstruc = list()
	listinstruc_d = list()
	bin_results_list = list()


	def __init__(self):
		self.openfile()
		self.clean_inst_list()
		self.ini_decode()
		self.create_bin_files()

	def openfile(self):
		print ("Bienvenido, te saludo por si no te habia saludado")
		print ("Ingrese el nombre del archivo a decodificar")
		#nombrear = input()
		nombrear = self.file_name

		while not os.path.isfile(nombrear):
	    		nombrear = input("Ingrese el nombre del archivo (.txt): ")
	    		if not ".txt" in nombrear:
	        		nombrear += ".txt"

		file = open(nombrear,"r")
		
		for linea in file:
			self.listinstruc_d.append(linea)
		
		file.close()

	def clean_inst_list(self):
		for line in self.listinstruc_d:
			if line.count(":"):
				splitted_line = line.split(":")
				tag = splitted_line[0].strip()
				# Agregar al diccionario el tag acompañado del numero de linea (Tamaño de listinstruc)
				self.tags_dict[tag] = len(self.listinstruc)+1
				#print("Tag", tag, "added with the value", len(self.listinstruc))
				
				if splitted_line[1].count(","):
					line = splitted_line[1]

			if line.count(","):
				self.listinstruc.append(line.strip())

	def ini_decode(self):
		for line_number in range(len(self.listinstruc)):
			line = self.listinstruc[line_number]

			if line.count(","):
				print(line)
				# Ver qué opcode es
				splitted_line = line.split(",")
				opcode = splitted_line[0].strip()

				if opcode in self.opcodes_dic["I"]:
					#print("Encontré un opcode I:", opcode)
					self.i_inst(opcode, splitted_line, line_number)
				elif opcode in self.opcodes_dic["R"]:
					#print("Encontré un opcode R:", opcode)
					self.r_inst(opcode, splitted_line)
				elif opcode in self.opcodes_dic["J"]:
					#print("Encontré un opcode J:", opcode)
					self.j_inst(opcode, splitted_line)
				else:
					print("El opcode no pertenece al ISA :(")

		return
					
	def i_inst(self, opcode, splitted_line, line_number):

		result_bin = ""
		reg_s = splitted_line[1].strip()
		reg_s = reg_s[1:]
		
		reg_t = splitted_line[2].strip()
		reg_t = reg_t[1:]
		immediate_val = splitted_line[3].strip()
		
		if opcode=="bne" or opcode=="beq":
			# Calcular el valor del salto
			immediate_val = self.tags_dict[immediate_val] - line_number
		elif immediate_val.count("x"):
			immediate_val = immediate_val.replace("x", "")
			immediate_val = int(immediate_val,base=16)

		if int(immediate_val) < 0:
			immediate_val = format(0xFF+1+int(immediate_val), "08b") 
		else:	
			immediate_val = format(int(immediate_val), "08b")
	    
		opcodes_i = self.opcodes_dic["I"]
		result_bin += opcodes_i[opcode]
		result_bin += format(int(reg_t), "03b")
		result_bin += format(int(reg_s), "03b")
		result_bin += immediate_val

		print(result_bin)
		self.bin_results_list.append(result_bin)

	def r_inst(self, opcode, splitted_line):
		result_bin = ""
		reg_s = splitted_line[2].strip()
		reg_s = reg_s[1:]
		
		reg_t = splitted_line[3].strip()
		reg_t = reg_t[1:]
		
		reg_d = splitted_line[1].strip()
		reg_d = reg_d[1:]
		opcodes_r = self.opcodes_dic["R"]
		result_bin += opcodes_r[opcode]
		result_bin += format(int(reg_t), "03b")
		result_bin += format(int(reg_s), "03b")
		result_bin += format(int(reg_d), "03b")
		result_bin += "00000"
		

		print(result_bin)
		self.bin_results_list.append(result_bin)
		
	def j_inst(self, opcode, splitted_line):
		result_bin = ""
		jmp_addr = splitted_line[1].strip()
		jmp_addr = self.tags_dict[jmp_addr]
		jmp_addr = format(int(jmp_addr), "014b")
		result_bin += self.opcodes_dic["J"][opcode]
		result_bin += jmp_addr
		print(result_bin)
		self.bin_results_list.append(result_bin)

	def create_bin_files(self):
		superString = ""

		for bin_line in self.bin_results_list:
			superString += bin_line
			superString += "\n"

		archivo1 = open((self.file_name + "-bin.txt"),"w")
		archivo1.write(superString)
		archivo2 = open((self.file_name + ".bin"),"wb")
		archivo2.write(bytes(superString,"utf-8"))
		archivo2.close()
		archivo1.close()
		
################### END OF CLASS #########################


def main():
    coordenada = lacoordenada()
    print("Hola :), se acabó")


if __name__ == "__main__":
    main()

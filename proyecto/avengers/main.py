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
	file_name = "codigo1.txt"
	opcodes_dic = {	"R":{"add":"0000", "and":"0010", "jr":"1010", "or":"1100", "sll":"1110", "srl":"1111"}, 
					"J":{"j":"0110", "jal":"0111"}, 
					"I":{"addi":"0001", "andi":"0011", "beq":"0100", "bne":"0101", "lb":"1011", "sb":"1110"} }

	def __init__(self):
		self.listinstruc = list()
		self.openfile()
		self.ini_decode()

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
			self.listinstruc.append(linea)
		
		file.close()

	def ini_decode(self):
		for line in self.listinstruc:
			print(line)

			# Agregar el uso de etiquetas

			if line.count(","):
				# Ver qué opcode es
				splitted_line = line.split(",")
				opcode = splitted_line[0].strip()

				if opcode in self.opcodes_dic["I"]:
					#print("Encontré un opcode I:", opcode)
					self.i_inst(opcode, splitted_line)
				elif opcode in self.opcodes_dic["R"]:
					#print("Encontré un opcode R:", opcode)
					self.i_inst(opcode, splitted_line)
				elif opcode in self.opcodes_dic["J"]:
					#print("Encontré un opcode J:", opcode)
					self.i_inst(opcode, splitted_line)
				else:
					print("El opcode no pertenece al ISA :(")

		return
					
	def i_inst(self, opcode, splitted_line):
		result_bin = ""
		reg_s = splitted_line[1].strip()
		reg_s = reg_s[1:]
		
		reg_t = splitted_line[2].strip()
		reg_t = reg_t[1:]
		immediate_val = splitted_line[3].strip()
		
		if line.count("x"):
		    immediate_val = immediate_val.replace("0x", "")
		    immediate_val = int(immediate_val, base=16)
	        immediate_val = format(immediate_val, "08b")
                resul_bin += reg_t
                resul_bin += reg_s
                resul_bin += immediate_val
                print (resul_bin)
                         

	def r_inst(self, opcode, splitted_line):
		reg_s = splitted_line[1].strip()
		reg_t = splitted_line[2].strip()
		reg_d = splitted_line[3].strip()

	def j_inst(self, opcode, splitted_line):
		jmp_addr = line[1].strip()
		#line_result = x
		#self.inst_integrator(line_result)
		
	def inst_integrator(self, line):
		pass


def main():
    coordenada = lacoordenada()
    print("Hola :), se acabó")


if __name__ == "__main__":
    main()

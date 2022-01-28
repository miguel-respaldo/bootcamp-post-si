
import os 


#text = open("/proc/cpuinfo","r")
text = open("cpuinfo","r")
lineas = text.readlines()


for line in lineas:
	n = line.index(":")
	if 'model name' in line:
		print(f"El Modelo Del Procesador Es: {line[n+2:]}", end="")
	if 'siblings' in line:
		print(f"El Numero De Procesadores Logicos Es: {line[n+2:]}", end="")	
	if 'cpu cores' in line:
		print(f"El Numero De Nucleos Es:{line[n+2:]}", end="")
		break

import os 


#text = open("/proc/cpuinfo","r")
text = open("cpuinfo","r")
lineas = text.readlines()


for line in reversed(lineas):
	n = line.index(":")
	if 'model name' in line:
		print(f"El Modelo Del Procesador Es: {line[n+2:]}", end="")
	if 'physical id' in line:
		print(f"El Numero De Procesadores Es De:{line[n+2:]}", end="")
	if 'stepping' in line:
		print(f"El Numero De Hilos Por Nucleo Es:{line[n+2:]}", end="")
	if 'siblings' in line:
		print(f"El Numero De Procesadores Logicos Es: {line[n+2:]}", end="")	
	if 'cpu cores' in line:
		print(f"El Numero De Nucleos Es:{line[n+2:]}", end="")
		break
	text.close()
		
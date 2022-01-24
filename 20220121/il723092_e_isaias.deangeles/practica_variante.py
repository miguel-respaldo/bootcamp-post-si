
import os 


text = open("/proc/cpuinfo","r")
lineas = text.readlines()


for line in lineas:
	if 'model name' in line:
		print(f"El Modelo Del Procesador Es: {line[13:]}", end="")
	if 'siblings' in line:
		print(f"El numero de Hilos Es: {line[11:]}", end="")	
	if 'cpu cores' in line:
		print(f"El numero de nucleos Es:{line[11:]}", end="")
		break
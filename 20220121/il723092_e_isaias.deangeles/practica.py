
import os 


text = open("cpuinfo","r")
lineas = text.readlines()


for line in lineas:
	if 'model name' in line:
		print(f"El Modelo Del Procesador Es: {line[13:]}", end="")
		break
for line in lineas:
	if 'cpu cores' in line:
		print(f"Los Nucleos de su procesador son: {line[10:]}", end="")
		break
for line in lineas:
    if 'siblings' in line:
        print(f"Los hilos de su procesador son: {line[11:]}", end="")
        break


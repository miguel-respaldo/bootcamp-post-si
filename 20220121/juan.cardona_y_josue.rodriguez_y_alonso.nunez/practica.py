#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Practica: Obtener informacion de un archivo y obtener informacion de el.
"""

#f = open('/proc/cpuinfo', 'r') #abrimos cpuinfo en modo lectura
f=open('/home/josuec/Documentos/Python/bootcamp-post-si/20220121/juan.cardona_y_josue.rodriguez_y_alonso.nunez/cpuinfo','r') 
f1 = open('cpuinfo_copia.txt', 'w')
f1.write(f.read())
f1.close()
f.close() 

#---------ABRIMOS EL ARCHIVO---------------------#
#informacion=open("/proc/cpuinfo")
informacion=open("cpuinfo")

texto= str(informacion.read())
print("CPU INFO:")
#---------Nombre del procesador------------------#
posicion=texto.find("model name")
posicion2=texto.find("\nstepping")

for x in range(posicion,posicion2):
     print(texto[x],end="")
print()

#---------Numero de procesadores lógicos---------#
procesador=int(texto.count("processor"))
print("logic processors number:",procesador)

#---------CPU CORES------------------------------#

posicion=texto.find("cpu cores")
posicion2=texto.find("\napicid")

for x in range(posicion,posicion2):
     print(texto[x],end="")
cores=int(texto[posicion2-1])
print()
#---------NUMERO DE PROCESADORES FISICOS---------#
posicion=texto.rfind("physical id")
posicion2=texto.rfind("siblings")
#print(posicion)
#print(posicion2)
for x in range(posicion,posicion2):
     print(texto[x],end="")
#---------NUMERO DE HILOS------------------------#

hilos=int(procesador/cores)
print("Threads per core:",hilos)
informacion.close()

#Lo ejecute en mi computadora y todo funciona correctamente. -Alonso 

#------------------------------------------------#
#Yo armé esto banda hasta ahorita solo jala el nombre del procesador y el número de procesadores chequen si jala en su compu 
 
#----------------------------------------------

#Hice la parte que copia el archivo 'cpuinfo', falta especificar el
#contenido que especifica la practica.
#Finalizada.

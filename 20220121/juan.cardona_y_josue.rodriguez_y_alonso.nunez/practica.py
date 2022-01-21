#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de un modulo
"""

f = open('/proc/cpuinfo', 'r') #abrimos cpuinfo en modo lectura
f1 = open('cpuinfo_copia.txt', 'w')
f1.write(f.read())
f1.close()
f.close() 

#---------------------------------------------
informacion=open("/proc/cpuinfo")
texto= str(informacion.read())
posicion=texto.find("model name")
#print(posicion)
posicion2=texto.find("\nstepping")
#print(posicion2)

print("CPU INFO:")
#---------Nombre del procesador--------
for x in range(posicion,posicion2):
     print(texto[x],end="")
print()

#---------Numero de procesadores--------
processor=texto.count("processor")
print("processors number:",processor)

informacion.close()

#Yo armé esto banda hasta ahorita solo jala el nombre del procesador y el número de procesadores chequen si jala en su compu 
 
#----------------------------------------------

#Hice la parte que copia el archivo 'cpuinfo', falta especificar el
#contenido que especifica la practica.

#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later


import string

opc = eval(input("\nOpcion 1 Archivo externo| any: el del sistema: "))
file="/proc/cpuinfo"
if opc==1:
    file="cpuinfo"


target_lines = ("model name","processor","cpu cores","siblings","physical id") # cadenas a buscar
cpu_specs = [] # lista para guardar busqueda

print("CPU INFO")
with open(file) as f:
    for line in f: #buscar en cada linea
        if len(cpu_specs) != len(target_lines):# si ya se hizo el primer recorrido
            for keyword in range(len(target_lines)): # si existe una de las palabaras de busqueda las lineas
                if target_lines[keyword] in line:     #a la linea le eliminamos la palabra clave
                    cpu_specs.append(line.strip(target_lines[keyword])) # agregar a la lista la linea que contiene la palabra cable
        elif target_lines[1] in line: # solo acutalizamos los procesadores logicos
            cpu_specs[0]=line.strip(target_lines[1])

physical = int(cpu_specs[0].strip(" :\n\t"))
print("Numero de Procesadores logicos: ",physical+1)
print("\nPysical Id ",cpu_specs[2])
print("Nombre del Procesador ",cpu_specs[1])
print("Numero de siblings ",cpu_specs[3])
print("Numero de Cores ",cpu_specs[4])


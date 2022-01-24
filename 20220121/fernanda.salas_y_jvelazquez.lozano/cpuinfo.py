#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later


print("CPU INFO")

target_lines = ("model name","processor","cpu cores","physical id") # cadenas a buscar
cpu_specs = [] # lista para guardar busqueda
with open("/proc/cpuinfo","r") as f:
    for line in f: #buscar en cada linea
        if len(cpu_specs) == len(target_lines):
            break # Si ya se encontro un elemento por cada elemento de busqueda , Salismos
        for keyword in range(len(target_lines)): # si existe una de las palabaras de busqueda las lineas
            if target_lines[keyword] in line:     #a la linea le eliminamos la palabra clave
                cpu_specs.append(line.strip(target_lines[keyword])) # agregar a la lista la linea que contiene la palabra cable


print("Numero de Procesadores logicos: ",cpu_specs[0])
print("Nombre del Procesador: ",cpu_specs[1])
print("Numero de Procesadores fisicos: ",cpu_specs[2])
print("Numero de Cores: ",cpu_specs[3])


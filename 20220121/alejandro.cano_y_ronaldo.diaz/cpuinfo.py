#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Esta practica es para obtener info del CPU
"""
import os

def main():
    """
    Se obtiene la informacion del archivo /proc/cpuinfo
    """
    print("Este programa obtiene informacion de los procesadores en tu maquina")
    #print("Puedes consultar esa informacion en el archivo generado")
    buscar = input("Ingresa el nombre del archivo, direccion/extension: \n")
    if not os.path.exists(buscar):
        print("El archivo no existe")
    else:
        cpu = open(buscar, 'r')
        print("Puedes consultar esa informacion en el archivo generado")
    #cpu = open("/proc/cpuinfo", 'r') # Abrir para eer archivo
    #cpu_info = str(cpu.read())
    #print(cpu_info)
    
    cpu_pfisicos = int(0)

    for linea in cpu:
        if "model name" in linea:
            cpu_modelo = linea[linea.find(":")+2 :-1]
        if "physical id" in linea:
            cpu_pfisicos += 1;     # suma el numero de procesadores fisicos
        if "siblings" in linea:
            cpu_plogicos = (linea[linea.find(":")+2:-1])
        if "cpu cores" in linea:
            cpu_cores = (linea[linea.find(":")+2:-1])
    
    cpu.close()
    '''
    print(cpu_modelo)
    print(cpu_pfisicos)
    print(cpu_plogicos)
    print(cpu_cores)
    print(int(cpu_pfisicos)/int(cpu_plogicos))
    '''

    # Crear el archivo para copiar la informacion
    info = open("info_cpu.txt", "w")    # si existe se reescribe
    info.write("\nEste archivo contiene la informacion de tu maquina: \n\n")
    info.write("Modelo del procesador: "+cpu_modelo+"\n")
    info.write("Numero de procesadores fisicos: "+str(cpu_pfisicos)+"\n")
    info.write("Numero de procesadores logicos: "+cpu_plogicos+"\n")
    info.write("Numero de cores: "+cpu_cores+"\n")
    info.write("Hilos por core: "+str(int(cpu_pfisicos)/int(cpu_plogicos))+"\n")
    info.close()

if __name__ == "__main__":
    main()


#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
script para obtener informacion del cpuinfo
"""

def main():
    #path="/proc/cpuinfo"
    path="../../20220124/cpuinfo-2"
    #path="../../20220124/cpuinfo"
    archivo = open(path,'r') #Abre el archivo

    #Busqueda de las palabras con la especificación requerida
    while(True):
        palabras=archivo.readline()
        if palabras.startswith("model name"):
            nombre_procesador=(palabras[palabras.find(":")+1:-1])

        if palabras.startswith("physical id"):
            physical_id=(palabras[palabras.find(":")+1:-1])

        if palabras.startswith("cpu cores"):
            cpu_cores=(palabras[palabras.find(":")+1:-1])

        if palabras.startswith("stepping"):
            stepping=(palabras[palabras.find(":")+1:-1])

        if palabras.startswith("siblings"):
            siblings=(palabras[palabras.find(":")+1:-1])
        if not palabras:
            break


    print("Nombre del procesador:"+nombre_procesador)
    print("Procesadores fisicos:"+physical_id)
    print("Numero de cores:"+cpu_cores)
    print("Hilos por core:"+stepping)
    print("Procesadores logicos:"+siblings)

    #Cierra el archivo
    archivo.close()

if __name__ == "__main__":
    main()

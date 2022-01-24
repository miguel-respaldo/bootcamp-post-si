#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Practica: CPU info
"""


def main():
    archivo = open("/proc/cpuinfo",'r') #Abre la informacion del sistema
    #texto = archivo.read()
    #print(texto)
    
    #Realiza la busqueda de las palabras que comiencen con lo que se necesita del archivo
    for palabras in archivo: 
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
            
    #Comienza a imprimir toda la informacion
    print("Nombre del procesador:"+nombre_procesador) 
    print("Procesadores fisicos:"+physical_id)
    print("Numero de cores:"+cpu_cores)
    print("Hilos por core:"+stepping)
    print("Procesadores logicos:"+siblings)
    archivo.close()

if __name__ == "__main__":
    main()


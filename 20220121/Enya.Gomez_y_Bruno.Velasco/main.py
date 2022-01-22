#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de un modulo
"""

def main():
    cpuinfo = open("/proc/cpuinfo", 'r') # Abrir para eer archivo
    archivo = open("out.txt", 'w') # Crear archivo

    for linea in cpuinfo:
        if linea.startswith("model name"):
            cadena = "Nombre del procesador: " + linea[linea.find(":")+2 :-1]
            archivo.write(cadena)
            print(cadena)
        
        if linea.startswith("physical id"):
            cadena = "No. de procesadores fisicos: " + linea[linea.find(":")+2 :-1]
            archivo.write(cadena)
            print(cadena)

        if linea.startswith("stepping"):
            cadena = "No. Cores: " + linea[linea.find(":")+2 :-1]
            archivo.write(cadena)
            print(cadena)

        if linea.startswith("siblings"):
            cadena = "No. Hilos: " + linea[linea.find(":")+2 :-1]
            archivo.write(cadena)
            print(cadena)

        if linea.startswith("cpu cores"):
            cadena = "No. de procesadores lógicos: " + linea[linea.find(":")+2 :]
            archivo.write(cadena)
            print(cadena)

    cpuinfo.close()
    archivo.close()


if __name__ == "__main__":
    main()
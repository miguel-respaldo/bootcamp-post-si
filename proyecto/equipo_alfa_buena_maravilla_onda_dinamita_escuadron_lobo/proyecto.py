#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Proyecto Final
Equipo:
    Antonio Josué Rodríguez Barera
    Javier de Alba Pérez
"""
import mnemonic
import os
import argparse

####Se abre el archivo###

#print (mnemonic.mnemonicos("add"))
#print (mnemonic.registros("x1"))

#####PRIMERO SE LEE LA ENTRADA DEL ARCHIVO####

matriz=[]

def main():
    """
    Función principal del programa
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("archivo", help="Archivo de entrada")
    parser.add_argument("-t", "--text",
                        action="store_true", dest="gen_texto", default=False,
                        help="Generar código en texto")
    parser.add_argument("-o", "--output",
                        action="store", dest="nombre_de_salida", default="salida.o",
                        help="Nombre de archivo de salida")

    args = parser.parse_args()
    
    if not os.path.exists(args.archivo):
        print(f"No se encuentra el archivo {args.archivo}")
        exit(1)
    else:
      archivo = open(args.archivo)
      contador = 0
      numero_instrucciones = int(args.archivo.count("v0"))
      for linea in archivo:
         lista=linea.split(",") 
         contador = 0
         for valor in lista:
            print("v{}".format(contador)," = ",valor.strip(),end="; ")
            contador += 1
         for i in range(numero_instrucciones):
                matriz[i].append(valor.strip())
         print()
         print(matriz)
            #print(val)
            #for i in range(numero_instrucciones):
            #   matriz.append([])
            #   for j in range(4):
            #     matriz[i].append(val)
         #print(matriz)
      archivo.close()


    print("Archivo:",args.archivo)
    print("Salida:",args.nombre_de_salida)
    print("en texto:",args.gen_texto)



if __name__ == "__main__":
    main()


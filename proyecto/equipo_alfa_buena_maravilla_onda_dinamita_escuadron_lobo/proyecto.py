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
import numpy as np
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
      j=0
      for linea in archivo:
          #separamos los argumentos con una coma
          lista=linea.split(",")
          #ejecutamos la funcion mnemonicos para obtener todos los opcode y tipo de función de cada instruccion en el archivo            
          opcode_tipo=mnemonic.mnemonicos(lista[0])
          #obtenemos el tipo de instruccion de cada instrucción del archivo
          tipo_instruccion=opcode_tipo[1]  
          #print(opcode_tipo)
          #print() 

          if(tipo_instruccion=="r"):
              print("mi opcode es",opcode_tipo[0])
          
          if(tipo_instruccion=="i"):
              print("mi opcode es",opcode_tipo[0])

          if(tipo_instruccion=="j"):
              print("mi opcode es",opcode_tipo[0])

      archivo.close()

    print("Archivo:",args.archivo)
    print("Salida:",args.nombre_de_salida)
    print("en texto:",args.gen_texto)



if __name__ == "__main__":
    main()

#print(a)
print(mnemonic.mnemonicos("addi"))
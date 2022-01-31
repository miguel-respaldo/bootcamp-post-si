#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Este traduce del ISA de MIPS a codigo máquina.
"""

import os
import argparse


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

    print("Archivo:",args.archivo)
    print("Salida:",args.nombre_de_salida)
    print("en texto:",args.gen_texto)

if __name__ == "__main__":
    main()


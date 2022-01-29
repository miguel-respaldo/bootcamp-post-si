#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
    Ejemplo de un modulo
"""

import datetime
import time


def main():
    """
        Main function
    """

    datos = [1, 4, 3, 2, 7, 6, 1, 3, 7, 4]
    print("Datos sin ordenar:", datos)
    datos_ordenados = sort(datos)
    print("Datos ordenados:", datos_ordenados)
    

def log(funcion):
    inicio = datetime.datetime.now()
    
    def wrapper(*args, **kwargs):
        f = open("log.txt","a")
        cantidad = len(args[0])
        f.write("Iniciando funcion con " + str(cantidad) + " elmentos a las " + str(inicio) + "\n")
        f.close()
        
        res = funcion(*args, **kwargs)
        return res

    fin = datetime.datetime.now()
    tiempo = inicio - fin
    f.write("Fin funcion a las " + str(fin) + " y tardo " + tiempo + " segundos" + "\n")
    return wrapper


@log
def sort(lista_datos):
    lista_datos.sort()
    return lista_datos


if __name__ == "__main__":
    main()


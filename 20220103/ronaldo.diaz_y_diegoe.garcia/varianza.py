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

    numeros=[]          # se declara una lista vacia
    varianza=0            # se declara variable de varianza
    sumatoria=0           # sumatoria auxiliar

    print("Este programa obtiene la varianza de 7 numeros")

    for x in range(7):  # se hace un for para obtener los 7 valores
        val=int(input("Ingrese el numero:"))
        numeros.append(val)
        
    n = len(numeros) #se obtiene el tamano de la lista
    
    sumatoria = sum(numeros)
        
    print(sumatoria)
        

if __name__ == "__main__":
    main()

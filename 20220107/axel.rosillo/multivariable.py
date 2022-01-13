#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Tarea: Multivariable
"""

def main():
    multivariable = int(input("Ingrese un numero: ")) #Se solicita el numero
    lista = ["Navidad","Zapato","Moto","Pez","Gato","Perro","Casa","Carro"] #Se declara la lista de variables
    binario = format ( multivariable , "08b" ) #Se convierte el numero a binario
    
    print(binario)
    
    for i in range(8): #Se imprime la lista de objetos
        if (int(binario[i]) == 1):
            print ( lista[i], end=" ")
            
    print("\n")

if __name__ == "__main__":
    main()


#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Práctica 1: Fórmula General para Ecuaciones Cuadráticas
"""
import math
from cmath import sqrt

def main():
    a = float(input ('Introduzca a:')) #Insertando a  
    b = float(input ('Introduzca b:')) #Insertando b
    c = float(input ('Introduzca c:')) #Insertando c

    aux_1 = (b**2)-(4*a*c)  #Calculando elementos dentro de la raíz

    if(aux_1) < 0:  #Caso por si el resultado es complejo
        print("Solución con el uso de números complejos:")
        aux_1 = sqrt(aux_1)
    else:           #Caso por si el resultado no es complejo
        print("Solución sin el uso de números complejos:")
        aux_1 = math.sqrt(aux_1)
    
    #Operaciones
    x1 = (-b+aux_1) / (2*a) 
    x2 = (-b-aux_1) / (2*a)
    
    #Mostrando los resultados
    print(x1) 
    print(x2)
    

if __name__ == "__main__":
    main()


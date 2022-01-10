#!/usr/bin/env python2
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Varianza muestreal s²
"""

def main():
    
    vector = []         # Declaración del vector de valores
    sumatoria = 0.0     # Declación de variables para el cálculo
    suma = 0.0
    promedio = 0.0

    tamanio = int(input("Cantidad de muestras: "))      # tamaño del vector
    for i in range(tamanio):
        entrada = float(input("Ingrese la entrada {}: ".format(i+1)))
        vector.append(entrada)

    for i in range(tamanio):        # Cálculo de la media del vector 
        suma += vector[i]
    promedio = suma / tamanio
    
    for i in range(tamanio):        # Calculo de la sumatoria de las distancias
        sumatoria += (vector[i] - promedio) ** 2

    print(sumatoria/tamanio-1)      # Muestra del resultado de la varianza



if __name__ == "__main__":
    main()

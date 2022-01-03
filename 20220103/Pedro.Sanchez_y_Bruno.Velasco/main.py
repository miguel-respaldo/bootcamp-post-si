#!/usr/bin/env python2
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Varianza muestreal
"""

def main():
    
    x = []
    sumatoria = 0.0
    suma = 0.0
    promedio = 0.0

    n = int(input("Cantidad de muestras: "))
    for i in range(n):
        entrada = float(input("Ingrese la entrada {}: ".format(i+1)))
        x.append(entrada)

    for i in range(n):
        suma += x[i]
    promedio = suma / n
    
    for i in range(n):
        #print((x[i] - promedio))
        sumatoria += (x[i] - promedio) ** 2

    print(sumatoria/n)



if __name__ == "__main__":
    main()


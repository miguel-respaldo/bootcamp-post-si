#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""

VARIANZA A 7 DATOS

"""

import statistics

def main():
    print("Hola Usuario, introduce 7 datos:")
    datos = list()

    for idx in range(7):
        print(f"Introduce el dato {idx}: ")
        datos.append(eval(input()))

    promedio = statistics.mean(datos)

    for dato in datos:
        sumatoria = (dato-promedio)**2

    resultado = (1/6)*(sumatoria)
    print(f"La varianza de los datos introducidos es: {resultado}")


if __name__ == "__main__":
    main()


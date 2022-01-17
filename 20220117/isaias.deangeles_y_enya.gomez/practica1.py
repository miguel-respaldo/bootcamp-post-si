#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de un modulo
"""
from operaciones import fibonacci_recursivo

numero = int(input("Ingrese la cantidad de valores:  "))




# Imprimir sin importar el resultado
#print(f"Imprimiendo serie hasta posición {posicion}")
#fibonacci_iterativo(posicion, True)
# Obtener valor pero no imprimir
#valor = fibonacci_iterativo(posicion, False)
#print(f"\nFibonacci de {posicion} con método iterativo es {valor}")
# Lo mismo de arriba pero con el método iterativo
valor = fibonacci_recursivo(numero)
print(f"Fibonacci de {numero} con método recursivo es {valor}")

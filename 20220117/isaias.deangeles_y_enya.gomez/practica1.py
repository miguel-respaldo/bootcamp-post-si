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


# Lo mismo de arriba pero con el método iterativo
valor = fibonacci_recursivo(numero)
print(f"Fibonacci de {numero} con método recursivo es {valor}")

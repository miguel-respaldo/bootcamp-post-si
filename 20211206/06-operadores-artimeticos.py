#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later


num1 = eval(input("Escribe y número: "))
num2 = eval(input("Escribe otro número: "))

modulo = num1 % num2
exponente = num1 ** num2
div_entera = num1 // num2
division = num1 / num2

print("El modulo de",num1, "con", num2, "es", modulo)
print("El exponente de",num1, "con", num2, "es", exponente)
print("La div_entera de",num1, "con", num2, "es", div_entera)
print("La división de",num1, "con", num2, "es", division)


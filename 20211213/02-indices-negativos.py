#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later


#         01234567890
cadena = "Hola Mundo!"
# negativos  87654321

print(cadena[-1])
print(cadena[-6])
print(cadena[-5:-2])
print("-->" + cadena[-2:-5] + "<--")

# Rangos -->  inicio:fin:incremento
print("-->" + cadena[-2:-5:-1] + "<--")

invertida = cadena[::-1]
print(invertida)



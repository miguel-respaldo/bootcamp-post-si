#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

# clases en python con constructores
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    x = 5

# Llamando al constructor
p1 = Persona("Ana", 25)

print(p1.nombre)
print(p1.edad)
print(p1.x)

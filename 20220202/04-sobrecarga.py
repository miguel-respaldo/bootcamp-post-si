#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

# clases en python con constructores
class Persona:

    def __init__(self, x, nombre = "sin nombre", edad = 0):
        self.nombre = nombre
        self.edad = edad
        self.x = x
        self.z = 100

    def imprime(self):
        print("Mi nombre es:", self.nombre)

    def imprime2(self):
        print("Soy Imprime 2")

    def suma(self, num1, num2):
        return num1 + num2

    def mas5(self, num1, num2):
        return num1 + num2 + self.x


class Persona2:
    nombre = ""
    edad = 0
    x = 5
    y = -5


# Llamando al constructor
p1 = Persona(-10, "Ana", 25)
p2 = Persona(5, edad=25, nombre="Juan")

print(p1.x)
print(p1.nombre)
print(p1.edad)
print(p2.x)
print(p2.nombre)
print(p2.edad)

# Agregar propiedad
p1.y = 100

# Borrar propiedad
del p1.y

# Borror el objeto
del p2



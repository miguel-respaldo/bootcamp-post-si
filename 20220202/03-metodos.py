#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

# clases en python con constructores
class Persona:
    def __init__(self, nombre = "sin nombre", edad = 0):
        self.nombre = nombre
        self.edad = edad
    x = 5

    def imprime(self):
        print("Mi nombre es:", self.nombre)

    def imprime2(self):
        print("Soy Imprime 2")

    def suma(self, num1, num2):
        return num1 + num2

    def mas5(self, num1, num2):
        return num1 + num2 + self.x

# Llamando al constructor
p1 = Persona("Ana", 25)
p1 = Persona("Ana")
p2 = Persona()

print(p2.nombre)
print(p1.nombre)
print(p1.edad)
print(p1.x)

p1.imprime()

p1.imprime2()

p1.x = 1000
p1.y = 1000

print(p1.suma(3,5))
print(p1.mas5(3,5))
print(p1.y)

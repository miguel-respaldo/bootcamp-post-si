#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

class Persona2:
    nombre = ""
    edad = 0
    x = 5
    y = -5

class Persona:
    def __init__(self, nombre="N/A", edad=0, x=5, y=-5):
        self.nombre = nombre
        self.edad = edad
        self.x = x
        self.y = y

lista = list()

lista.append(Persona2())

lista[0].nombre = "algo"
lista[0].edad = 20

lista.append(Persona2())

lista[1].nombre = "otro"
lista[1].edad = 29

lista.append(Persona())

lista[2].nombre = "mas"
lista[2].edad = 39

lista.append(Persona("init",10))

for persona in lista:
    print(f"Nombre: {persona.nombre}")
    print(f"edad: {persona.edad}")





#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# SPDX-License-Identifier: GPL-3.0-or-later

tupla = ("manzana", "platano", "naranja")
print(tupla)

solo_uno = ("manzana", )
print(type(solo_uno))

no_es_tupla = ("manzana")
print(type(no_es_tupla))

tupla_varios_datos = ("abc", 33, True, 3.1416, "def")

# Constructor
una_tupla = tuple(("manzana", "platano", "naranja"))

print(una_tupla[1])

print("Actualizar tupla")
# Actualizar una tupla
lista = list(tupla)
lista[1] = "kiwi"
tupla =  tuple(lista)

print(tupla)

melon = ("melon",)
tupla += melon

print(tupla)

(cadena, entero, boleano, flotante, cadena2)  = tupla_varios_datos
print(cadena)
print(entero)

for x in tupla_varios_datos:
    print(x)

for i in range(len(tupla)):
    print(tupla[i])

# que pasa si "sumo" dos tuplas (t3 = t1 + t2)
# que pasa si "multiplico" una tupla  ( t3 = 3 * t1)



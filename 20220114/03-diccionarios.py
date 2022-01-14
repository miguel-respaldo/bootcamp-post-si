#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# SPDX-License-Identifier: GPL-3.0-or-later

diccionario = {
        "marca": "Ford",
        "modelo": "Mustang",
        "año": 1964
        "colores": ["rojo", "blanco", "azul"]
        }

# Desde Pytohn 3.7 los diccionarios son ordenados

print(diccionario)
print(len(diccionario))
print(diccionario["marca"])
print(diccionario.get("marca"))

lista = diccionario.keys()
print(lista)

diccionario["año"] = 2020
diccionario.update({"año": 2022})


diccionario["puertas"] = 2
print(diccionario)

diccionario.update({"radio": "AM/FM"})
print(diccionario)

diccionario.pop("radio")
print(diccionario)

for i in diccionario:
    print(i)

for x in diccionario:
    print(diccionario[x])

for x in diccionario.values():
    print(x)

for x in diccionario.keys():
    print(x)

for x,y in diccionario.items():
    print(x,y)


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
tupla + = melon

print(tupla)

(cadena, entero, boleano, flotante, cadena2)  = tupla_varios_datos
print(cadena)
print(entero)

for x in tupla_varios_dtos:
    print(x)

for i in range(len(tupla))
    print(tupla[i])

# que pasa si "sumo" dos tuplas (t3 = t1 + t2)
# que pasa si "multiplico" una tupla  ( t3 = 3 * t1)



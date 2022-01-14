#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# SPDX-License-Identifier: GPL-3.0-or-later

diccionario = {
#        key : value ,
        "marca": "Ford",
        "modelo": "Mustang",
        "año": 1964,
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
diccionario.update({"puertas": 2})
diccionario.update({"llantas": 4})
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


# Aqui se copia el puntero/referencia del diccionario
otro_diccionario = diccionario

# Aqui se hace una copia
otro_diccionario = diccionario.copy()

otro_diccionario = dict(diccionario)




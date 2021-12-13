#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later


cadena = "Hola,Mundo!"

lista = cadena.split(",")

print(lista)
print(lista[0])
print(lista[1])

# Comma Separte Value
csv = "Producto,Precio,Cantidad,Provedor"

lista = csv.split(",")
print(lista)
print(len(lista))
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])


print("----------------_")
lista = cadena.split("la")
print(lista)
lista = cadena.split("o")
print(lista)
lista = cadena.split("la ")
print(lista)
lista = cadena.split("Mundo")
print(lista)

print("----------------_")
cadena = "La casa de la esquina es azul"
lista = cadena.split(" ")
print(len(lista))
print(lista)


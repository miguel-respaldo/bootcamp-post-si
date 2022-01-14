#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# SPDX-License-Identifier: GPL-3.0-or-later

conjunto = {"manzana", "platano", "naranja"}
print(conjunto)
print(type(conjunto))

conjunto = {"manzana", "platano", "naranja", "manzana"}
print(conjunto)

set_varios_datos = {"abc", 33, True, 3.1416, "def"}

# Constructor
un_conjunto = set(("manzana", "platano", "naranja")) # doble parentesis

# No se puede
#print(un_conjunto[1])

for x in un_conjunto:
    print(x)


print("naranaja" in un_conjunto)


un_conjunto.add("kiwi")
print(un_conjunto)

lista = ["manzana", "platano", "manzana"]
tupla = ("manzana", "platano", "manzana")
set_varios_datos.update(un_conjunto) # un_conjunto puede ser otro tipo iterable
set_varios_datos.update(lista) # un_conjunto puede ser otro tipo iterable
set_varios_datos.update(tupla) # un_conjunto puede ser otro tipo iterable
print(set_varios_datos)


set_varios_datos.remove("abc")
set_varios_datos.remove("def")
print(set_varios_datos)

set_varios_datos.discard("abc") # No da error si no existe


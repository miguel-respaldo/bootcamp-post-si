#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

a = "   Hola Mundo!  "
print("-->" + a.strip() + "<--")

cadena = "Hola Mundo!"
print(cadena.replace("H","L"))
print(cadena.replace("Hola","Adios") )
print(cadena.replace("o","u"))
print(cadena)

print("----------------------------")

txt = """ Hola {},
Buenos dias, como esta
blabla

espero que usted {} tenga {}
saludos"""

numero = 8

print(txt)
print("----------------------------")
print(txt.format("Maria", "Maria", numero))
print("----------------------------")
print(txt.format("Maria", "Juan", numero))
print("----------------------------")
print(txt.replace("{}","Juan"))
print("----------------------------")
print( txt.replace(" ","").replace("\n","") )

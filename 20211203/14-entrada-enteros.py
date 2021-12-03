#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

texto =                 input("Escribe un texto: ")
cualquier_numero = eval(input("Escribe un número cualquiera: "))
entero   =          int(input("Escribe un número entero: "))
flotante =        float(input("Escribe un número flotante: "))
complejo =      complex(input("Escribe un número y lo haré complejo: "))


print( type(texto) ) 
print( type(cualquier_numero) ) 
print( type(entero) ) 
print( type(flotante) ) 
print( type(complejo) ) 

print(texto) 
print(cualquier_numero) 
print(entero)
print(flotante)
print(complejo)

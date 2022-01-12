#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

frutas = 0
animales = 0
frutas_y_animales = 0

MANZANA = 1   # 1
PERA    = 2   # 1 << 1
MANGO   = 4   # 1 << 2
NARANJA = 8   # 1 << 3
GUAYABA = 16  # 1 << 4
PERRO   = 32  # 1 << 5
GATO    = 64  # 1 << 6
TIBURON = 128 # 1 << 7
BURRO   = 1 << 8
CABALLO = 2**9 # 1 << 9


frutas |= MANZANA
frutas |= PERA
frutas |= GUAYABA

frutas_y_animales = frutas_y_animales | MANZANA | PERA | GUAYABA | GATO | TIBURON

animales |= GATO
animales |= TIBURON

print("Frutas = {}  = {:b}".format(frutas, frutas))
print("Frutas y Animales = {} = {:b}".format(frutas_y_animales, frutas_y_animales))
print("Animales = {} = {:b}".format(animales, animales))

if frutas & MANGO != MANGO:
    print("no compre mango")
else:
    print("si compre mango")


if frutas_y_animales & PERA == PERA:
    print("Si compre pera")
else:
    print("No compre pera")


if animales & PERRO == PERRO:
    print("Si compre un perrro")
else:
    print("No compre un perrro")

animales |= PERRO
print("Animales = {} = {:b}".format(animales, animales))

if animales & PERRO == PERRO:
    print("Si compre un perrro")
else:
    print("No compre un perrro")

animales ^= PERRO
print("Animales = {} = {:b}".format(animales, animales))

if animales & PERRO == PERRO:
    print("Si compre un perrro")
else:
    print("No compre un perrro")

animales |= PERRO
animales &= ~PERRO
print("Animales = {} = {:b}".format(animales, animales))
print("perro = {} = {:b}".format(PERRO, PERRO))

if animales & PERRO == PERRO:
    print("Si compre un perrro")
else:
    print("No compre un perrro")


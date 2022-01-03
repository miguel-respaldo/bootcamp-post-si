#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later


lista = ["uno", "dos", "tres", "cuatro", "cinco"]

cantidad = len(lista)

for elemento in range(cantidad):
    # Imprimimos el último elento 2 veces
    if elemento == cantidad-1:
        print(lista[elemento])

    # Imprimimos el primer elemento 2 veces
    if elemento == 0:
        print(lista[elemento])
    print(lista[elemento])




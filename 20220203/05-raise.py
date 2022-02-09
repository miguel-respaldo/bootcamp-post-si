#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

x = 1 ## es valor -1

if x < 0:
    raise Exception("No se puede numeros negativos")


x = "hola"

if not type(x) is int:
    raise TypeError("Solo se adminten enteros")



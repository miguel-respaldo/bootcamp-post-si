#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later


cantidad = 3
articulo = 567
precio = 49
txt = "El costo de {1} piezas del articulo con número {0} es de {2:.2f} pesos"

print(txt.format(articulo, cantidad,precio))

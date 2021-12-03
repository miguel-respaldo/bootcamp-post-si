#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later


precio = 49
txt = "El precio es {} pesos"

print(txt.format(precio))

txt = "El precio es {:.2f} pesos"
print(txt.format(precio))


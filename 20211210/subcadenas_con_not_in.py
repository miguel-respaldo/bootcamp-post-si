#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later


txt = "Las mejores cosas en la vida son gratis!"

print("gratis" not in txt)
print("free" not in txt)


if "free" not in txt:
    print("Si, 'free' NO esta en la cadena")


if "gratis" not in txt:
    print("Si, 'gratis' NO esta en la cadena")

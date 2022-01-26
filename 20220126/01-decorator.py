#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later


def f():
    print("Hola")

def otra(una_fun):
    una_fun()

# function aliasing
con_otro_nombre = f
otra(f)

#f()
#print(f)

con_otro_nombre()





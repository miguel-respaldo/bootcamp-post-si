#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

x=5

try:
    print(x)
    #f = open("holaMundo")
    #f = open()
except NameError:
    print("La variable no esta definida")
except FileNotFoundError:
    print("No esta el archivo")
except:
    print("Ocurrio una excepción")
else:
    print("Todo esta bien")


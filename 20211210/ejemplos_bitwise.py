#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

x = 22

print("x      =        {:>6b}".format(x))
el_and = x & 4
print("x & 4  = {:>3d}  = {:>6b}".format(x & 4, el_and))
print("x | 1  = {:>3d}  = {:>6b}".format(x | 1, x | 1))
print("x ^ 4  = {:>3d}  = {:>6b}".format(x ^ 4, x ^ 4))
print("~x     = {:>3d}  = {:>6b}".format(~x, ~x))
# x =   22    =   0...0000010110
# ~x          =   1...1111101001   

#  complemento a 2 -> invertir los valores y sumar 1
# y =   23    =   0...0000010111
#                 1...1111101000 invertir los valores
# y =  -23    =   1...1111101001 sumar 1
print("x << 1 = {:>3d}  = {:>6b}".format(x << 1, x << 1))
print("x >> 2 = {:>3d}  = {:>6b}".format(x >> 2, x >> 2))




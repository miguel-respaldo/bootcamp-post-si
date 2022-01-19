#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

f = open("demo.txt", "r")
print(f.read(5))
print(f.read(5))
print(f.read(5))
print("------")

f.seek(0)
print(f.read(5))
print(f.read(5))
print(f.read(5))
f.seek(5)
print("------")
print(f.read(5))


#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

matriz = [[1,2],[3,4]]

# 0 [ 1, 2 ]  
# 1 [ 3, 4 ]

matriz[0][0] = 5
matriz[0][1] = 6
matriz[1][0] = 7
matriz[1][1] = 8

print(matriz[0][0]) # 1
print(matriz[0][1]) # 2
print(matriz[1][0]) # 3
print(matriz[1][1]) # 4

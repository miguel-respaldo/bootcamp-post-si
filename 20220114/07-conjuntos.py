#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# SPDX-License-Identifier: GPL-3.0-or-later

import random

lista = [random.randrange(1,50) for x in range(50)]

unicos = set(lista)

print(len(lista))
print(len(unicos))



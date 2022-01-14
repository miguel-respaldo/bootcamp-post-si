#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

import random
import time

lista = [random.randint(1,50) for x in range(10000)]

beginning = time.time()
lista.sort()
end = time.time()
elapsed_time = round((end-beginning)*1000, 3)

print("\nLista ordenada:\n\n", lista)

print("\nTiempo de ejecución del ordenamiento por defecto en python:", elapsed_time, "milisegundos")


#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

import os

file = open('/proc/cpuinfo', 'r')
flag= [True,True]

for x in file:
    if "model name" in x and flag[0]:
        print("Nombre del procesador: " + x.replace("model name","").replace(":","").strip())
        flag[0] = False
    if "cpu cores" in x and flag[1]:
        print("No. Cores: " + x.replace("cpu cores","").replace(":","").strip())
        flag[1] = False

file.close()

#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

import os
actual=0
proce=0
#file = open('/proc/cpuinfo', 'r')
#file = open('cpuinfo', 'r')
file = open('cpuinfo-2', 'r')
flag= [True,True,True,True]

for x in file:
    if "model name" in x and flag[0]:
        print("Nombre del procesador: " + x.replace("model name","").replace(":","").strip())
        flag[0] = False
    if "cpu cores" in x and flag[1]:
        print("No. Cores: " + x.replace("cpu cores","").replace(":","").strip())
        flag[1] = False
    if "physical id" in x:
        numerofisico=int(x.replace("physical id","").replace(":","").strip())
        if numerofisico > actual:
            actual=numerofisico
    if "siblings" in x and flag[2]:
        print("No. de hilos: " + x.replace("siblings","").replace(":","").strip())
        flag[2]= False
    if "processor" in x:
        proce+=1
    
    
print("No. de procesadores fisicos: " + str(numerofisico + 1))
print("No. de procesadores lógicos: " + str(proce))

file.close()

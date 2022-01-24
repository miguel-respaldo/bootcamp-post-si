#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
script para obtener informacion del cpuinfo
"""
import sys

def main():
    path="/proc/cpuinfo"
    arch=open(path)
    while(True):
        linea = arch.readline()
        print(linea)
        if not linea:
            break:
    arch.close()


if __name__ == "__main__":
    main()


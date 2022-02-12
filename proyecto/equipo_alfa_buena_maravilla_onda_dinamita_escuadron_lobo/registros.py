#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Registros

"""

def registros(reg):
    if reg=="x0":
        num_reg=0x0

    elif reg=="x1":
        num_reg=0x1
        
    elif reg=="x2":
        num_reg=0x2
        
    elif reg=="x3":
        num_reg=0x3
        
    elif reg=="x4":
        num_reg=0x4
        
    elif reg=="x5":
        num_reg=0x5
        
    elif reg=="x6":
        num_reg=0x6
        
    elif reg=="x7":
        num_reg=0x7
    else:
        num_reg=-1
        
    return (num_reg)

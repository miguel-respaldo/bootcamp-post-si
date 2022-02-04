#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

#diccionario para instrucciones tipo I y J
mnemonicos = {"addi":8, "addiu":9, "andi": 12, "beq":4, "bne": 5, "lbu": 36,
        "lhu": 37, "ll": 48, "lui": 15, "lw": 35, "ori": 13, "slti": 10,
        "sltiu": 11, "sb": 40, "sc": 56, "sh": 41,"sw": 43, "lwc1":49,
        "ldc1": 53, "swc1": 57, "sdc1": 61, "j": 2, "jal": 3}


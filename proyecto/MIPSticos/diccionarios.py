#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

#diccionario para instrucciones tipo I y J
mnemonicos_dict_I = {"addi":8, "addiu":9, "andi": 12, "beq":4, "bne": 5, "lbu": 36,
        "lhu": 37, "ll": 48, "lui": 15, "lw": 35, "ori": 13, "slti": 10,
        "sltiu": 11, "sb": 40, "sc": 56, "sh": 41,"sw": 43, "lwc1":49,
        "ldc1": 53, "swc1": 57, "sdc1": 61}

mnemonicos_dict_J = {"j": 2, "jal": 3}

#diccionario para los registros

registers = {"$zero": 0, "$at": 1, "$v0": 2, "$v1": 3, "$a0": 4, "$a1": 5, "$a2":
        6, "$a3": 7, "$t0": 8, "$t1": 9, "$t2": 10, "$t3": 11, "$t4": 12, "$t5":
        13, "$t6": 14, "$t7": 15, "$s0": 16, "$s1": 17, "$s2": 18, "$s3": 19,
        "$s4": 20, "$s5": 21, "$s6": 22, "$s7": 23, "$t8": 24, "$t9": 25, "$k0":
        26, "$k1": 27, "$gp": 28, "$sp": 29, "$fp": 30, "$ra": 31 }

#diccionario para funct
funct = {"add": 32, "addu": 33, "sub": 34, "subu": 35, "and": 36, "or": 37, "nor": 39,
	 "slt": 42, "sltu": 43}

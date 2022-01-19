#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
    Funciones para ejecución de Factorial y de la función de Fibonacci
"""

def factorial(num):
    """
        Función factorial
    """
    
    if(num == 0): return 1

    if(num < 0): return "ERROR :("

    if(num > 1):
        result = num * factorial(num-1)
    else:
        result = num

    return result


def fibonacci(num1, num2, num3, num4):
    """
        Función fibonacci
    """
    
    if(num == 0): return 0

    if(num3==1 or num3==2):
        result = 1
    
    if(num3 > 2):
        fibonacci(num2, num1+num2, num3, num4+1)

    return result


def fibonacci_2(num):
    """
        Función fibonacci
    """
    
    if(num == 0): return 0

    if(num==1 or num==2):
        result = 1
    elif(num > 2):
        result = fibonacci_2(num-1)+fibonacci_2(num-2)
    else:
        return "ERROR :("

    return result

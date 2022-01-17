#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de un modulo
"""

def fibonacci(n):
   
#first two terms are first and second
    valor1=0
    valor2=1
    sum=0
    count=1
    print("Fibonacci Sequence: ")
    while(count<=n):    
        print(sum)
        count+=1
        valor1=valor2
        valor2=sum
        sum=valor1+valor2

def factorial(n):
    producto=1
    for i in range(n):
        producto *=(i+1)
    return producto

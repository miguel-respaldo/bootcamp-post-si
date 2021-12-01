#!/usr/bin/env python3

x = "increible"

def unaFuncion():
    global x
    x="fantastico"
    print("Python es " + x)


unaFuncion()
print("Python es "+x)

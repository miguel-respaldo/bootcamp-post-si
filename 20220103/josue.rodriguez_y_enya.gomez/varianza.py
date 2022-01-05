#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de un modulo
"""

a = float(input("inserte el primer valor:"))  #pedimos los valores al usuario
b = float(input("inserte el segundo valor:"))
c = float(input("inserte el tercer valor:"))
d = float(input("inserte el cuarto valor:"))
e = float(input("inserte el quinto valor:"))
f = float(input("inserte el sexto valor:"))
g = float(input("inserte el septimo valor:"))

n =int(7)                     #Definimos el numero de elementos totales 
promedio = (a+b+c+d+e+f+g)/n  #calculamos el promedio 
  
valores = [a,b,c,d,e,f,g]     #hacemos una lista con los valores 

tam=len(valores)              #calculamos el tamaño de la lista

sumatoria=0                   #inicializamos la variable sumatoria
for xi in range(tam):         #iteramos en cada elemento de la lista "valores" 
   suma=(valores[xi]-promedio)**2  #calculamos el xi-promedio de cada iteracion
   sumatoria=sumatoria+suma   #hacemos la sumatoria de (xi-promedio)**2
                              
varianza=(sumatoria/(n-1))    #realizamos el calculo de la varianza 
print("La varianza es = {:.4f}".format(varianza)) # imprimimos el valor de la varianza 






#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

lista = [] #creamos una lista vacia

sumatoria = 0 #inicializamos en cero sumatoria

for i in range(7):
    dato = int(input("Ingrese un valor: "))
    lista.append(dato) #agregamos los datos ingresados a nuestra lista
    sumatoria += dato #se realiza la sumatoria de los datos

media = sumatoria / 7 #calculamos la media

desviacion = 0 #inicializamos nuestra variable en 0

for j in range(7):
    desviacion += (lista[j]-media)**2 #calculamos la desviacion


varianza = desviacion / 7

print("La varianza es: ", varianza)


#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""

Calculo de la Varianza muestral de 7 Datos

"""
# utilizada para obtener la media aritmetica o promedio
import statistics

def main():
    print("Bienvenido, Introduce 7 datos para calcular la varianza muestral:")
    datos = list()
    #Ciclo para obtener los 7 numeros 
    for idx in range(7):
        print(f"Introduce el dato {idx+1}: ")
    #Guardar el numero que introdujo el usuario en la lista
        datos.append(eval(input()))
    #calculo del promedio 
    promedio = statistics.mean(datos)
    
    #Ciclo para obtener la sumatoria con la formula de la imagen
    Resultado_Sum = 0
    for dato in datos:
    #calculo de la operacion del interior de la sumatoria
        operando_interno = (dato-promedio)**2
        Resultado_Sum += operando_interno
    #Calculo de la operacion de la varianza muestral
    resultado_final = (1/6)*(Resultado_Sum)
    #Calculo utilizando la opcion de la libreria statistics
    Variancia= statistics.variance(datos,promedio)
    
    text="la varianza muestral de los datos introducidos es: {:3f}"
    print(text.format(Variancia))
    print(text.format(resultado_final))






if __name__ == "__main__":
    main()


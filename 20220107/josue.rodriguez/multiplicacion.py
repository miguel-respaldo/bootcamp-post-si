#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de multiplicación de matrices
"""

print("Bienvenido, este programa multiplica 2 matrices")
matrizA=[]
matrizB=[]
matrizresul=[]

print("Matriz A")
FMA=(int(input("  Inserte el número de filas de la matriz A:")))
CMA=(int(input("  Inserte el número de columnas de la matriz A:")))
print()

print("Matriz B")
FMB=(int(input("  Inserte el número de filas de la matriz B:")))
CMB=(int(input("  Inserte el número de columnas de la matriz B:")))
print()

if CMA==FMB: # verificamos si la operación es posible
    #Llenamos los valores de la matriz A
    for i in range(FMA): 
        matrizA.append([])
        for j in range(CMA):
            numero = eval(input("Ingresa un número para la posición ({},{}) de la matriz: ".format(i,j)))
            matrizA[i].append(numero)

    #Imprimimos los valores de la Matriz A
    print()
    print("Matriz A")
    for i in range(len(matrizA)):
        print("[ ", end="")
        for j in range(len(matrizA[i])):
           print(matrizA[i][j], end=" ")
        print("]")
    print()
    
    #Llenamos los valores de la matriz B
    for i in range(FMB): 
        matrizB.append([])
        for j in range(CMB):
            numero = eval(input("Ingresa un número para la posición ({},{}) de la matriz: ".format(i,j)))
            matrizB[i].append(numero)

    #Imprimimos los valores de la Matriz B 
    print()
    print("Matriz B")
    for i in range(len(matrizB)):
        print("[ ", end="")
        for j in range(len(matrizB[i])):
           print(matrizB[i][j], end=" ")
        print("]")
    print()
    
    #RESULTADO ES UNA MATRIZ DE FMA x CMB
    #Creamos una matriz del tamaño Filas de matriz A x columnas de la Matriz B
    for i in range(FMA):
        matrizresul.append([])
        for j in range(CMB):
            matrizresul[i].append(0)
            
    #Realizamos la multiplicación y la sumatoria para cada elemento de la nueva matriz         
    for columnaB in range(CMB): 
        for filaA in range(FMA):
            resultado=0         #reiniciamos el resultado anterior

    #hacemos la suma para cada elemento yendo desde las coordenadas (0,0),(0,1),(0,2)...(1,0),(1,1),(1,2).... 
            for columnaA in range(CMA):
              #realizamos la sumatoria de la primer fila con la primer columna y así sucesivamente
              resultado+=matrizA[filaA][columnaA]*matrizB[columnaA][columnaB]
            #print("({},{}){}".format(i,c,resultado))
            #print("i",i)
        #print("c",c)
              #almacenamos el resultado en la posición de la columna
            matrizresul[filaA][columnaB]=resultado
    
              #matrizresul[filaA][columnaB].append(resultado)
    #Imprimimos los valores de la Matriz resultado 
    print()
    print("Matriz AxB")
    for i in range(FMA):
        print("[ ", end="")
        for j in range(CMB):
           print(matrizresul[i][j], end=" ")
        print("]")
    
else:
    print("Dimensiones no válidas")
    

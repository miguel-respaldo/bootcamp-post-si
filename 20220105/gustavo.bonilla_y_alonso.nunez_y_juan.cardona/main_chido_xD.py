#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""

    Matriz_Caracol

"""

def main():
    print("Hola!! Este programa muestra en consola una serie de números dentro de una matríz\nLos números están ordenados en forma de caracol :)\n")
    tamano_matriz = int(input("Introduce el tamaño deseado para las filas y columnas de la matriz de caracol (número entero): "))
    
    ################### Inicialización de Variables #######################

    matriz_caracol = []             # Matríz a lenar
    fila_d = 0                      # Variable para iteraciones de izquierda a derecha
    columna_d = 0                   # Variable para iteraciones de izquierda a derecha
    fila_c = 1                      # Variable para iteraciones de arriba a abajo
    columna_c = tamano_matriz-1     # Variable para iteraciones de arriba a abajo
    columna_b = tamano_matriz-2     # Variable para iteraciones de derecha a izquierda
    fila_b = tamano_matriz-1        # Variable para iteraciones de derecha a izquierda
    columna_a = 0                   # Variable para iteraciones de abajo a arriba
    fila_a = tamano_matriz-2        # Variable para iteraciones de abajo a arriba
    iteraciones = (tamano_matriz*2)-1 # Cantidad total de elementos en la matríz
    iteracion = 1                   # Número de iteración actual (a, b, c, d)                
    contador = 1                    # Siguiente elemento para llenar en la matriz
    estado_giro = 3                 # Estado actual (a, b, c, d) 

    #######################################################################

    for i in range(tamano_matriz):  # Generación de matriz de ceros
        matriz_caracol.append([])
        for j in range(tamano_matriz):
            matriz_caracol[i].append(0)

    #for idx in range(tamano_matriz): print(matriz_caracol[idx])

    # Inicia ciclo para llenar la matríz
    for idx in range(iteraciones):
        if estado_giro == 0:    # Estado actual es de abajo a arriba?
            #print("AAAA")
            for jdx in range(tamano_matriz-((iteracion-1)//2)-1):
                matriz_caracol[fila_a-jdx][columna_a] = contador    # Asignación del dato
                contador += 1
            
            fila_a -= 1         # Asignación de nuevo valor de inicio para fila
            columna_a += 1      # Asignación de nuevo valor de inicio para columna
        elif estado_giro == 1:  # Estado actual es de derecha a izquierda?
            #print("BBBB")
            for jdx in range(tamano_matriz-((iteracion-1)//2)):
                matriz_caracol[fila_b][columna_b-jdx] = contador    # Asignación del dato
                contador += 1
            
            fila_b -= 1         # Asignación de nuevo valor de inicio para fila
            columna_b -= 1      # Asignación de nuevo valor de inicio para columna
        elif estado_giro == 2:  # Estado actual es de arriba a abajo?
            #print("CCCC")
            for jdx in range(tamano_matriz-((iteracion-1)//2)-1):
                matriz_caracol[fila_c+jdx][columna_c] = contador    # Asignación del dato
                contador += 1
            
            fila_c += 1         # Asignación de nuevo valor de inicio para fila
            columna_c -= 1      # Asignación de nuevo valor de inicio para columna
        else:                   # Estado actual es de izquierda a derecha
            #print("DDDD")
            for jdx in range(tamano_matriz-((iteracion-1)//2)):
                matriz_caracol[fila_d][columna_d+jdx] = contador    # Asignación del dato
                contador += 1
            
            fila_d += 1         # Asignación de nuevo valor de inicio para fila
            columna_d += 1      # Asignación de nuevo valor de inicio para columna

        iteracion += 1          # Cambio de iteración
        jdx = 0                 # Restablecimiento de la variable jdx

        if estado_giro:
            estado_giro -= 1    # Restablecimiento de estado
        else:
            estado_giro = 3     # Cambio de estado

    print("\n\nMatríz resultante:\n")

    #for idx in range(tamano_matriz): print(matriz_caracol[idx])

    # Despliegue de matríz resultante en consola
    for i in range(tamano_matriz): 
        print('[', end='\t')
        for j in range(tamano_matriz):
            print(matriz_caracol[i][j], end='\t')
        print(']')


if __name__ == "__main__":
    main()

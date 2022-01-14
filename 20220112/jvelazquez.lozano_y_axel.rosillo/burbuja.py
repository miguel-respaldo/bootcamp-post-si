#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Practica: Ordenamiento
"""
import random
import time

def burbuja(ordenar):   # Funcion de ordenamiento burbuja
    for i in range(1,len(ordenar)): # Ciclo de 1 a la longitud de la lista
        for j in range(0,len(ordenar)-i):
            if(ordenar[j+1] < ordenar[j]): # Compara si el siguiente elemento es menor
                aux=ordenar[j];
                ordenar[j]=ordenar[j+1];
                ordenar[j+1]=aux; # Hace el intercambio
    print (ordenar)

def main():

    lista = random.sample(range(0, 1000), 1000) # Crea una lista de numeros aleatorios
    print(lista)
    
    inicio = time.time() # Inicializa el contador de tiempo
    burbuja(lista); # Ordena con burbuja
    fin = time.time() # Guarda el tiempo final
    tiempo_burbuja = fin-inicio # Calcula el tiempo de ejecucion 
    
    inicio = time.time() # Inicializa el contador de tiempo
    lista.sort() # Ordena con sort
    #print (lista)
    fin = time.time()  # Guarda el tiempo final
    tiempo_sort = fin-inicio  # Calcula el tiempo de ejecucion 
    
    print("El algoritmo burbuja tuvo un tiempo de: ")
    print(tiempo_burbuja)
    
    print("La funcion sort tuvo un tiempo de: ")
    print(tiempo_sort)
    
    
    

if __name__ == "__main__":
    main()


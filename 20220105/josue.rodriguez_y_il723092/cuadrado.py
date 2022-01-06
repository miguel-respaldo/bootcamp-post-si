#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later


n=int(input("inserte el tamaño del cuadrado nxn:")) #definimos el tamaño del cuadrado nxn

matriz= []          #definimos una matriz vacia
cont = 1            #inicializamos la variable contador en 1
derecha,izquierda,abajo,arriba=0,1,2,3
fila=0              #inicializamos la fila de partida
columna=0           #inicializamos la columna de partida
direccion=derecha   #definimos la direccion inicial

for i in range(n):  # hacemos una matriz de 0s de nxn
    matriz.append([])
    for j in range(n):
        matriz[i].append(0)

while cont<=n**2:
    
    if direccion==derecha:  #comenzamos con la direccion de partida 
        if columna<n and matriz[fila][columna]==0: # verificamos si el numero de columna es menor a n que es el tope de la columna y verificamos si hay 0s
           matriz[fila][columna]=cont #si hay 0s los rellena con la variable cont 
           #print("entre1:",cont) 
           cont+=1                    #incrementamos la variable cont en 1
           columna+=1                 #aumentamos columna para iterar entre las posiciones de la primer fila
        else:               #si no se cumple la condicion inicial entonces:
          direccion=abajo   #cambiamos de direccion 
          fila+=1           #incrementamos el valor de la fila
    
    elif direccion==abajo:  #si cambiamos de direccion hacia abajo entonces:
        if fila<n and matriz[fila][columna-1]==0: # verificamos si el numero de fila es menor a n que es el tope de la fila y verificamos si hay 0s
            #print("fila",fila)
            #print("columna",columna)
            matriz[fila][columna-1]=cont #si hay 0s los rellena con la variable cont
            #print("entre:2",cont)
            cont+=1                   #incrementamos la variable cont en 1
            fila+=1                   #aumentamos fila en 1 para iterar entre las posiciones de la fila de la ultima columna                     
        else:                         #si no se cumple la condicion inicial entonces:
            direccion=izquierda       #cambiamos de direccion
            columna-=1                #disminuimos ahora el valor de columna de la ultima fila
    
    elif direccion==izquierda:        #si cambiamos de direccion hacia la izquierda entonces:
        if columna>0 and matriz[fila-1][columna-1]==0: # verificamos si el numero de columna es mayor a 0 que es el tope de la columna y verificamos si hay 0s
            matriz[fila-1][columna-1]=cont      #si hay 0s los rellena con la variable cont
            #print("entré3:",cont)                
            cont+=1                             #incrementamos la variable cont en 1
            columna-=1        #dismimuimos el valor de columna para ir de derecha a izquierda
        else:                 #si no se cumple la condicion inicial entonces:
            direccion=arriba  #cambiamos de direccion hacia arriba
            fila-=1           #cambiamos de fila de abajo hacia arriba
    
    elif direccion==arriba:          #si cambiamos de direccion hacia arriba entonces:
        if fila>0 and matriz[fila-1][columna]==0: # verificamos si el numero de fila es mayor a 0 que es el tope de la fila y verificamos si hay 0s
            matriz[fila-1][columna]=cont #si hay 0s los rellena con la variable cont
            #print("entre4:",cont)
            cont+=1               #incrementamos la variable cont en 1
            fila-=1               #iteramos entre los valores de fila de abajo hacia arriba
        else:                     #si no se cumple la condicion inicial entonces:
            direccion=derecha    #cambiamos otra vez de direccion hacia la derecha haciendo el caracol 
            columna+=1           #aumentamos el valor de columna para seguir iterando    

#print(matriz)              
for i in range(n):              #imprimimos la matriz en espiral
    print(matriz[i])

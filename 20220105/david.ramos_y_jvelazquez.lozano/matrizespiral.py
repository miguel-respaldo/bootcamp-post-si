#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later


def main():
    n = int(input("Ingre el tam de matriz: "))

    k=1
    
    
    matriz = []
    for x in range(n):
        matriz.append([])
        for y in range(n):
            matriz[x].append(0)
    
    for x in range(n):
        print("[",end="")
        for y in range(n):
            print(matriz[x][y],end="")
        print("]")
    
    lim = n//2
    for i in range(lim):
     
        j = i
        while j < n-i:
            print(f"i: {i} j: {j}")
        #for x in range(n-i): # arriba
            matriz[i][j] = k
            k += 1
            j+=1
            
    
        j = i
        while j < n-i:
        #for x in range(n-i): # derecha
            matriz[j][n-i+1] = k
            k += 1
            j+=1
        
        j = n-i+1
        while j >= i+1:
            matriz[n-i+1][j] = k
            k+=1
            j=j-1

        j= n-i+1
        while j >= i+1:
            matriz[j][i] = k
            k+=1
            j=j-1

    if n%2 == 1:
        i = (n+1)/2
        matriz[i][i] = n*n


    for x in range(n):
        print("[",end="")
        for y in range(n):
            print(matriz[x][y],end="")
        print("]")
        
    """

    int i,j,a[100][100],n,k;
    printf ("Ingrese el valor de n:");
    scanf("%d",&n);
    k=1;
    for(i=1;i<=n/2;i=i+1)
    {
                 para (j = i; j <= n-i; j = j + 1) // arriba*   
        {
            a[i][j]=k;
            k=k+1;
        }
                 para (j = i; j <= n-i; j = j + 1) // derecha*
        {
            a[j][n-i+1]=k;----
            k=k+1;
        }
                 para (j = n-i + 1; j> = i + 1; j = j-1) // a continuación
        {
            a[n-i+1][j]=k;
            k=k+1;
        }
                 para (j = n-i + 1; j> = i + 1; j = j-1) // izquierda
        {
            a[j][i]=k;
            k=k+1;
        }
    }
    if(n%2==1)
    {
        i=(n+1)/2;
        a[i][i]=n*n;
    }
    for(i=1;i<=n;i=i+1)
    {
        for(j=1;j<=n;j=j+1)
            printf("%4d",a[i][j]);
        printf("\n");
    }
    printf("\n");
"""


if __name__ == "__main__":
    main()


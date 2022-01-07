def main():
    n = int (input ( "Ingrese la dimension de la matriz >> " ) ) #Pedimos dimension de matriz
    
    matriz = [[0 for i in range(n)] for j in range(n)] #Realizamos un llenado de nuestra matriz con 0's
    nivel = 0
    coordenada = 0

    
        
    num = n - (nivel * 2) - 1
    temp = coordenada

    for i in range(num):
        temp += 1
        matriz[nivel][i+nivel] = temp
        matriz[nivel+i][n-nivel-1] = temp + num
        matriz[n-nivel-1][n-nivel-i-1] = temp + num * 2
        matriz[n-nivel-i-1][nivel] = temp + num * 3


        for i in matriz: #Realizamos la impresion de la matriz con un formato adecuado (de cuadrado)
            for j in i:
                print('%3s' % j, end='')
            print("")

    nivel += 1
    coordenada += num * 4

    num = n - (nivel * 2) - 1   #Declaramos variables utiles para el llenado de la matriz
    temp = coordenada
                    
    for i in range(num):        #proceso de llenado de matriz de 4 en 4 numeros 
        temp += 1           
        matriz[nivel][i+nivel] = temp
        matriz[nivel+i][n-nivel-1] = temp + num
        matriz[n-nivel-1][n-nivel-i-1] = temp + num * 2
        matriz[n-nivel-i-1][nivel] = temp + num * 3


        for i in matriz: #Realizamos la impresion de la matriz con un formato adecuado (de cuadrado)
            for j in i:
                print('%3s' % j, end='')
            print("")

if __name__ == "__main__":
    main()


import numpy #libreria que da soporte para crear vectores y matrices
#multidimencionales

def main():
   

    f_A = int(input("Ingrese el numero de filas de la matriz A: \n"))
    c_A = int(input("Ingrese el numero de columnas de la matriz A: \n"))

    matrizA = numpy.random.randint(0, 1000, size=(f_A, c_A)) #Llena matriz A con numeros aleatorios entre 0 y 1000
    print(matrizA)
    
    f_B = int(input("Ingrese el numero de filas de la matriz B: \n"))
    m_B = int(input("Ingrese el numero de columnas de la matriz B: \n"))

    matrizB = numpy.random.randint(0, 1000, size=(f_B, m_B)) #Llena matriz B con numeros aleatorios entre 0 y 1000
    print(matrizB)
    
    if c_A == f_B: #para que la multiplicacion se lleve acabo, las columnas de la matriz A y las filas de la matriz B deben ser del mismo tamaño
        print("El resultado de multiplicar A * B es:")
        result = []
        for i in range(len(matrizB[0])): #Ciclo para calcular la matriz resultante
            total = 0
            for j in range(len(matrizA)): 
                total += matrizA[j] * matrizB[j][i]
            result.append(total)


        for i in result: #Ciclo para imprimir
            print("[", end="")
            for j in i:
                print('%3s' % j, end=' ')
            print("]")
    else:
        print("Estas 2 matrices no se pueden multiplicar")


if __name__ == "__main__":
    main()

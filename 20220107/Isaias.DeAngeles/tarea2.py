# programa que pide 2 matrices y las multiplica 
import random
matrix1 = [[0,-7,3],
		   [2,4,-1],
		   [12,7,-6]]


matrix2 = [[5,4,-3],
           [0,-6,10],
           [-2,8,11]]
m1_filas = int(input("Introduzca el numero de filas de la matriz 1 --> "))
m1_columnas = int(input("Introduzca el numero de columnas de la matriz 1 --> "))
m2_filas = int(input("Introduzca el numero de filas de la matriz 2 --> "))
m2_columnas = int(input("Introduzca el numero de columnas de la matriz 2 --> "))

matrix1 = [[random.randint(-10,10) for i in range(m1_filas)] for j in range(m1_columnas)]
matrix2 = [[random.randint(-10,10) for i in range(m2_filas)] for j in range(m2_columnas)]

print ("La matriz 1 es: ")
for i in matrix1: #Realizamos la impresion de la matriz con un formato adecuado (de cuadrado)
        for j in i:
            print('%3s' % j, end='')
        print("")
print ("La matriz 2 es: ")
for i in matrix2: #Realizamos la impresion de la matriz con un formato adecuado (de cuadrado)
        for j in i:
            print('%3s' % j, end='')
        print("")



if len(matrix1[0]) == len(matrix2):
	
	matrix3 = [[0 for i in range(len(matrix1))] for j in range(len(matrix2[0]))]

	for a in range(len(matrix1)):
		for b in range(len(matrix2[0])):
			for c in range(len(matrix1[0])):
				matrix3[a][b] += matrix1[a][c] * matrix2[c][b]
else:
	print("Bro esta matriz no se puede multiplicar")

for i in matrix3: #Realizamos la impresion de la matriz con un formato adecuado (de cuadrado)
        for j in i:
            print('%4s' % j, end='')
        print("")	

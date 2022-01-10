# programa que pide 2 matrices y las multiplica 

matrix1 = [[0,-7,3],
		   [2,4,-1],
		   [12,7,-6]]


matrix2 = [[5,4,-3],
           [0,-6,10],
           [-2,8,11]]

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
            print('%3s' % j, end='')
        print("")	

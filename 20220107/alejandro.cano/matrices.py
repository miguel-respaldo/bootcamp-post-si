# MULTIPLICACION DE 2 MATRICES

# FILAS MAT A
FILAS_A=int(input("Introduce número de filas para MATRIZ A: "))
print("\n")

# COLUMNAS MAT A
COLUMNAS_A=int(input("Introduce número de columnas para MATRIZ A: "))
print("\n")

# COLUMNAS MAT B
"""
  (porque para vida de multiplicar matrices, el numero de columnas de 
  la primera matriz, debe ser igual al numero de filas de la segunda)
"""
COLUMNAS_B=int(input("Introduce numero de columnas para MATRIZ B: "))
print("\n")

# MATRIZ A (inicializada en ceros)
A=[]
for i in range(FILAS_A):
    # con append agrega ceros en el arreglo creado para A
    A.append([0]*COLUMNAS_A)

# MATRIZ B (inicializada en ceros)
B=[]
for i in range(COLUMNAS_A):
    # con append agrega ceros en el arreglo creado para B
    B.append([0]*COLUMNAS_B)

# INTRODUCE VALORES PARA MATRIZ A
for i in range(FILAS_A):
    for j in range(COLUMNAS_A):
        A[i][j]=float(input("Introduce los valores de A en (%d, %d): " % (i,j)))

# INTRODUCE VALORES PARA MATRIZ B
print("\n")
for i in range(COLUMNAS_A):
    for j in range(COLUMNAS_B):
        B[i][j]=float(input("Introduce los valores de B en (%d, %d): " % (i,j)))

# MATRIZ C (inicializada en ceros, aqui se guardará el resultado de A x B)
C=[]
for i in range(FILAS_A):
    # con append agrega ceros en el arreglo creado para C
    C.append([0]*COLUMNAS_B)

# MULTIPLICACION DE MATRICES A y B

for i in range(FILAS_A):
    for j in range(COLUMNAS_B):
        for k in range(COLUMNAS_A):
            C[i][j] += A[i][k] * B[k][j]

# MATRIZ FINALE

print("\n MATRIZ RESULTANTE: \n")

for i in range(FILAS_A):
    R=[]
    for j in range(COLUMNAS_B):
        # con append agrega los valores de C en el nuevo arreglo R
        R.append(C[i][j])
    print(R)
print("\n")

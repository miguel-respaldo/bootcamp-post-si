from random import randint

filasMatrizA=int(input("Ingrese el numero de filas de la 1ra matriz: "))
columMatrizA=int(input("Ingrese el numero de columnas de la 1ra matriz: "))

matrizA = list()

for f in range(0,filasMatrizA):
    matrizA.append(list())
    for c in range(0,columMatrizA):
       matrizA[f].append(randint(1,30))

for fila in range(0,filasMatrizA):
    print("[", end=" ")
    for columna in range(0,columMatrizA):
        print(f" {matrizA[fila][columna]} ", end="")
    print("]")

filasMatrizB=int(input("Ingrese el numero de filas de la 2da matriz: "))
columMatrizB=int(input("Ingrese el numero de columnas de la 2da matriz: "))


matrizB = list()
for f in range(0,filasMatrizB):
    matrizB.append(list())
    for c in range(0,columMatrizB):
       matrizB[f].append(randint(1,30))

for fila in range(0,filasMatrizB):
    print("[", end=" ")
    for columna in range(0,columMatrizB):
        print(f" {matrizB[fila][columna]} ", end="")
    print("]")

if filasMatrizA == columMatrizB:
# rellenar con espacios vacíos
    print("\n PRODUCTO DE MATRICES \n")
    producto = []
    for i in range(0,filasMatrizB):
        producto.append([])
        for j in range(0,columMatrizB):
            producto[i].append(None)
    # Rellenar el producto
    for c in range(columMatrizB):
        for i in range(0,filasMatrizA):
            suma = 0
            for j in range(0,columMatrizA):
                suma += matrizA[i][j]*matrizB[j][c]
            producto[i][c] = suma

    for fila in range(0,columMatrizB):
        print("[", end=" ")
        for columna in range(0,filasMatrizA):
            print(f" {producto[fila][columna]} ", end="")
        print("]")
else:
    print("Nope, no se multiplican")



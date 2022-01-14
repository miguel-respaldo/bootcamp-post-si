import random
A=list()
def burbuja(A): #ordena la lista A
    for i in range(1,len(A)):
        for j in range(0,len(A)-i):
            if(A[j+1] < A[j]):
                aux=A[j]
                A[j]=A[j+1]
                A[j+1]=aux
    print("lista ordenada")
    print(A)
tamanio=int(input("ingrese el tamaño de la lista a ordenar: \n"))
A=[random.randrange(1,50) for i in range (tamanio)] #genera lista de valores random
print("lista random") 
print(A) 
burbuja(A #Muestra la lista ordenada)

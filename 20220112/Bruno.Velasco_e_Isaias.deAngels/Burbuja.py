import random
import time



numeros = int(input("Ingresa el tamano de lista que deseas --> "))
lista = []

for n in range(numeros):
	lista.append(random.randint(0,999))
print(lista)


start_time = time.time() #Ordenamiento con Burbuja
for n in range(len(lista)-1):
	for j in range(len(lista)-1):
		if lista[j] > lista[j+1]:
			temp = lista[j]
			lista[j]=lista[j+1]
			lista[j+1]=temp

print("La lista ordenada con burbuja es:   ")
print(lista)
print(f"El tiempo logrado fue de {time.time() - start_time}")



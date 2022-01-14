import random
import time



numeros = int(input("Ingresa el tamano de lista que deseas --> "))
lista = []

for n in range(numeros):
	lista.append(random.randint(0,999))
print(lista)


start_time = time.time()
print("La lista ordenada con Sort() es:   ")
lista.sort()
print(lista)
print(f"El tiempo logrado fue de {time.time() - start_time}")
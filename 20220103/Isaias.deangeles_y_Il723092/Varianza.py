


numeros = [] #Declaracion de nuestra lista que contendra los numeros introducidos

for numero in range(7):
	numeros.append(int(input(f"Ingresa un numero {numero}-> "))) # pedimos al usuario 7 numeros 
sumatoria = 0 # inicializacion de la variable
for numero in numeros: # recorremos nuestra lista para realizar la sumatoria 
	sumatoria += numero # se suman todos los valores
sumatoria /=7 # se obtiene el promedio
varianza = 0 # inicialización de la variable
for numero in numeros: 
	varianza += (numero - sumatoria)**2 # cálculo de la parte de sumatoria

varianza /= 6 # division final

print(f"la varianza es = {varianza}") 
#print (sumatoria)



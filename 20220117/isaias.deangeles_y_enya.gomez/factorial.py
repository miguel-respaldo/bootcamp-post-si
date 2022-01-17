def factorial(n):
	if n > 1:
		n = n * factorial(n -1)
	return n 

n = input("Ingresa El numero que deseas hacer factorial")
print(factorial(5))
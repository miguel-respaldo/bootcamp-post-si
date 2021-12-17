import math



a = float(input("escribe el valor de a: "))
b = float(input("escribe el valor de b: "))
c = float(input("escribe el valor de c: "))

determinante=2*a

res1=complex((-b+math.sqrt(b**2-(4*a*c)))/determinante)
res2=complex((-b-math.sqrt(b**2-(4*a*c)))/determinante)

	
#if (determinante<0):
#	res1=complex((-b+math.sqrt(b**2-(4*a*c)))/determinante)
#	res2=complex((-b-math.sqrt(b**2-(4*a*c)))/determinante)
#else:
#	res1=(-b+math.sqrt(b**2-(4*a*c)))/determinante
#	res2=(-b-math.sqrt(b**2-(4*a*c)))/determinante


print ('El Valor de la Raiz 1 es:',res1)
print ('El Valor de la Raiz 2 es:',res2)
import math

def formula_general(a, b, c):
    if a == 0:
        print("El valor de a no puede ser igual a 0")
        raise ValueError("A no puede ser igual a 0")
    else:
        formula = abs(b ** 2 - 4 * a * c) # si el numero resultante es negativo
        #entonces es complejo, es el discriminante
        if formula >= 0: # es positivo, dos soluciones
           if formula == 0: #si es igual a 0 solo hay una solucion
               resultado = (-b + math.sqrt(formula)) / 2 * a
               print("La raiz unica es {:.3f}".format(resultado))
           else:
            	x1 = (-b + math.sqrt(formula)) / (2 * a)
            	x2 = (-b - math.sqrt(formula)) / (2 * a)
            	print("La raíz real x1 es {:.3f}".format(x1))
            	print("La raíz real x2 es {:.3f}".format(x2))
        else:
              formula = abs(formula)
              parteReal = -b / (2 * a)
              parteImaginaria = math.sqrt(siReal) / (2 * a)
              print("La raíz compleja x1 es {:.3f} + {:.3f}i".format(parteReal, parteImaginaria))
              print("La raíz compleja x2 es {:.3f} - {:.3f}i".format(parteReal, parteImaginaria))

print("---------- CALCULADORA DE FORMULA GENERAL ----------")
a = float(input("Ingresa el valor de a: "))
b = float(input("Ingresa el valor de b: "))
c = float(input("Ingresa el valor de c: "))

formula_general(a,b,c)

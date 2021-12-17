import math


def formula_general(a, b, c):
    if a == 0:
        print("El valor de a no puede ser igual a 0")
        raise ValueError("A no puede ser igual a 0")

    formula = abs ( b ** 2 - 4 * a * c)  # si el numero resultante es negativo no hay solucione reales

    if formula == 0: #si es igual a 0 solo hay una solucion
        resultado = (-b + math.sqrt(formula)) / 2 * a
        print("La raiz unica es {:.3f}".format(resultado))

    elif formula > 0: #si es mayor a 0 entonces hay dos soluciones
        resultado = (-b + math.sqrt(formula)) / (2 * a)
        resultado_2 = (-b + math.sqrt(formula)) / (2 * a)
        print("La raiz es {:.3f}".format(resultado))
        print("La raiz es {:.3f}".format(resultado_2))
    else:
        x1 = (-b + math.sqrt(formula)) / (2 * a)
        x2 = (-b - math.sqrt(formula)) / (2 * a)
        print("La raiz real x1 es {:.3f}+i".format(x1))
        print("La raiz real x2 es {:.3f}-i".format(x2))


    
print("---------- CALCULADORA DE FORMULA GENERAL ----------")
a = float(input("Ingresa el valor de a: "))
b = float(input("Ingresa el valor de b: "))
c = float(input("Ingresa el valor de c: "))
formula_general(a,b,c)

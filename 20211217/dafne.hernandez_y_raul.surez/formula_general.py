import math


def formula_general(a, b, c, d):
    if a == 0:
        print("El valor de a no puede ser igual a 0")
        raise ValueError("A no puede ser igual a 0")

    formula = b ** 2 - 4 * a * c  # si el numero resultante es negativo no hay solucione reales

    if d == 0:
        resultado = (-b + sqrt(formula)) / 2 * a
        print("La raiz unica es {:.3f}".format(resultado))

    elif d > 0:
        resultado = (-b + sqrt(formula)) / 2 * a
        resultado_2 = (-b + sqrt(formula)) / 2 * a
        print("La raiz es {:.3f}".format(resultado))
        print("La raiz es {:.3f}".format(resultado_2))

    
print("---------- CALCULADORA DE FORMULA GENERAL ----------")
a = float(input("Ingresa el valor de a: "))
b = float(input("Ingresa el valor de b: "))
c = float(input("Ingresa el valor de c: "))
d = float(input("Ingresa el resultado de la ecuacion: "))


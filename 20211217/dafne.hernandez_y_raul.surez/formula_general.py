import math


def formula_general(a, b, c, d):
    pass


print("---------- CALCULADORA DE FORMULA GENERAL ----------")
a = float(input("Ingresa el valor de a: "))
b = float(input("Ingresa el valor de b: "))
c = float(input("Ingresa el valor de c: "))
d = float(input("Ingresa el resultado de la ecuacion: "))

if a == 0:
    print ("El valor de a no puede ser igual a 0")
else: 
    siReal = b**2 - 4 * a * c #si el numero resultante es negativo no hay
    if siReal >= 0:         # soluciones reales
        if siReal == 0:
            x = -b / (2*a)
            print("La raiz unica es {:.3f}".format(x))


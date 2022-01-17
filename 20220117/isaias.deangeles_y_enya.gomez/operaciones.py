def fibonacci_iterativo(posicion, debe_imprimir):
    actual = 0
    siguiente = 1
    for x in range(posicion + 1):
        if debe_imprimir:
            print(str(actual) + ",", end="")
        temporal = actual
        actual = siguiente
        siguiente = siguiente + temporal
    return temporal


def fibonacci_recursivo(posicion):
    if posicion < 2:
        return posicion
    return fibonacci_recursivo(posicion - 1) + fibonacci_recursivo(posicion - 2)

def factorial(n):
    if n > 1:
        n = n * factorial(n -1)
    return n 


'''
Hacer un programa que guarde hasta 8 variables boleanas en un entero.

Las variables son:

Carro -> on/off 1
Casa -> on/off 
Perro -> on/off 4
Gato -> on/off 8
Pez -> on/off 16
Moto -> on/off 32
Zapato -> on/off 64
Navidad -> on/off 128
'''
#lista con las palabras
variables = ["Carro", "Casa", "Perro", "Gato", "Pez", "Moto", "Zapato", "Navidad"]

#pedimos los numeros
multivariable = int(input("Ingrese un numero entero: "))

bin = "{:b}".format(multivariable) #transformamos los numeros a binario
print(bin)

#hacemos las iteraciones
for i in range(8):

    if bin[i] == "1": 
        print(variables[i],"on,", end=" ") #si es 1 encendemos
    else:
        print(variables[i],"off,", end=" ") #si no, apagamos

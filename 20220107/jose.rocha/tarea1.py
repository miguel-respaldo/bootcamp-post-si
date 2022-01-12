#TAREA 1
#Rocha Fuentes José Francisco

print('''Las variables a tratar son:
Carro   -->  ON/OFF  1   -->  00000001
Casa    -->  ON/OFF  2   -->  00000010
Perro   -->  ON/OFF  4   -->  00000100
Gato    -->  ON/OFF  8   -->  00001000
Pez     -->  ON/OFF  16  -->  00010000
Moto    -->  ON/OFF  32  -->  00100000
Zapato  -->  ON/OFF  64  -->  01000000
Navidad -->  ON/OFF  128 -->  10000000  ''')
variables = ("Navidad","Zapato","Moto","Pez","Gato","Perro","Casa","Carro")

numero = int(input("Inserte el numero: "))

#se castea a binario
multivariables = format(numero,"b")
print(f"\n{multivariables}\n")

#se vuelve string
multivariables=multivariables.zfill(8) 

#se recorre el arreglo
for x in range(8):

    #se muestra lo que está encendido y apagado
    if multivariables[x] == "0":  
         print(f"OFF {variables[x]}")
    else:
         print(f"ON  {variables[x]}")

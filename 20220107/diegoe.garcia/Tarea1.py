lista = ("Navidad","Zapato","Moto","Pez","Gato","Perro","Casa","Carro") 


num = int(input("Ingrese un numero del 1 al 8: "))


multivariable = format(num,"b") # cambio de formato a binario
print(f"\n{multivariable}\n")

#cambiamos la variable a string
multivariable=multivariable.zfill(8) # llenando la cadena en 0 en caso de ser menor a 128, .zfill devuelve una cadena que especifica la longitud de la cadena original justificado a la derecha, frontal con relleno de ceros.

for x in range(8): # recorrimiento del arreglo 

    if multivariable[x] == "0": 
        print(f"off {lista[x]}")
    else:
        print(f"on {lista[x]}")

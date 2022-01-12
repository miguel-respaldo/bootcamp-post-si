
#tupla de las plabras
items = ("Navidad","Zapato","Moto","Pez","Gato","Perro","Casa","Carro")


num = int(input("Ingrese un num: "))


multivariable = format(num,"b") # casteo del numero a binario
print(f"\n{multivariable}\n")

#nota esto cambia la variable a string
multivariable=multivariable.zfill(8) # llenando la cadena en 0 en caso de ser menor a 128

for x in range(8): # recorremos el arreglo 

    if multivariable[x] == "0": # 
        print(f"off {items[x]}")
    else:
        print(f"on {items[x]}")

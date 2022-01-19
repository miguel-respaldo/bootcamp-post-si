import os

archivo = input("Introduce el nombre del archivo que quieras copiar -> ")


if os.path.exists(archivo):
    f = open(archivo, "r")
    contenido = f.read()  # se guarda en una variable
    f.close()

    f = open("copia2.txt","w")
    f.write(contenido) # se escribe contenido
    print("se copio")
    f.close()

    f  = open("copia2.txt")

    for x in f:
        print(x.strip())

else:

    print("El archivo no existe")

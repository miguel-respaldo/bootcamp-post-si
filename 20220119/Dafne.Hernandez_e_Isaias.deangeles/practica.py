


import os


archivo = input("Introduce el nombre del archivo que quieras copiar -> ")


if os.path.exists(archivo):
    contenido = open(archivo, "r")
    copia = open("copia.txt", "x")
    copia.write(contenido)
    copia.close()

    os.remove(archivo)
else:
    print("El archivo no existe")


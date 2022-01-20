import os

archivo = input("Introduce el nombre del archivo que quieras copiar -> ")


if os.path.exists(archivo):
    f = open(archivo, "r")
    contenido = f.read()  # se guarda en una variable
    f.close()
    nuevo = archivo[:-4] + "-copia" + archivo[-4:]
    #for n in range(len(archivo)):
    #    if archivo[n] == ".":
    #        if archivo[n+1] =="t":
    #            if archivo[n+2] =="x":
    #                nuevo = archivo[:n] + '-Copia' + archivo[n:]
    f = open(nuevo,"w")
    f.write(contenido) # se escribe contenido
    print("se copio")
    f.close()

    f  = open(nuevo)

    for x in f:
        print(x.strip())

else:

    print("El archivo no existe")

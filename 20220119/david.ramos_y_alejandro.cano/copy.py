import os

buscar = input("Ingresa el nombre del archivo, direccion/extension")

if not os.path.exists(buscar):
    print("El archivo no existe")
else:

    archivo = open(buscar, "r")



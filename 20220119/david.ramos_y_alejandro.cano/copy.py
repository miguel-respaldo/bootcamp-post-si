import os

buscar = input("Ingresa el nombre del archivo, direccion/extension: \n")

if not os.path.exists(buscar):
    print("El archivo no existe")
else:

    archivo = buscar.replace(".txt", "-copia.txt")
    new_name = "cp " + buscar + " " + archivo
    os.system(new_name)
    print("Archivo copia creado")
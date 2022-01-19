


import os


archivo = imput("Introduce el nombre del archivo que quieras copiar")

if os.path.exists(archivo):
    os.remove(archivo)
else:
    print("El archivo no existe")


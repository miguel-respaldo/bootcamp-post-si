
import os

nombre = input('Introduzca el nombre del archivo a copiar: ')
index = nombre.find('.') #encuentro el punto de la extension
nombre_copia = nombre[:index] + '_copia' + nombre[index:] # creo el nombre de la copia
if os.path.exists(nombre):  #compruebo si el archivo existe
    f = open(f'{nombre}', 'r') #guardo contenido del archivo a una variable
    f.close()       
    f_copia = open(f'{nombre_copia}', 'a') #creo archivo con nombre de copia
    f_copia.write(f'{f}')   #copio el contenido de var en archivo
    f_copia.close()

    print(f'copie el contenido de {nombre}, en {nombre_copia}')
else:
    print(f'el archivo {nombre} no existe')

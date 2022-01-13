resto=list()    #Guardar los resto de modulo, numero binario o bander
Menu = ''' 
       ¿que quieres activar?\n
       Carro             > 1\n
       Casa              > 2\n
       Perro             > 4\n
       Gato              > 8\n
       Pez               > 16\n
       Moto              > 32\n
       Zapato            > 64\n
       Navidad           > 128\n
       '''
print(Menu)
Multivariable = int(input("\nIntroduce un numero del 0 al 255\n"))

while Multivariable >=1: # comprobar si la var ya vale 0     
    resto.append(Multivariable%2)   #se agrega el residuo a la lista resto
    Multivariable=Multivariable//2  #se divide entre 2 la var

while len(resto) < 8:   #se rellena la lista resto con 0
    resto.append(0)


if resto[0] == 1:               #bit menos significativo 
    print('Se encendio el carro\n')
if resto[1] == 1:
    print('Se encendio la casa\n')
if resto[2] == 1:
    print('Se encendio el perro\n')
if resto[3] == 1:
    print('Se encendio el gato\n')
if resto[4] == 1:
    print('se encendio el pez\n')
if resto[5] == 1:
    print('Se encendio la Moto\n')
if resto[6] == 1:
    print('Se encendio el zapato\n')
if resto[7] == 1:               #bit mas significativo 
    print('Se encencio la navidad\n')


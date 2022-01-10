carro = 1 
casa = 2 
perro = 4
gato = 8
pez = 16
moto = 32
zapato = 64
navidad = 128
multivariable = 255
contenido = []
items = [carro,casa,perro,gato,pez,moto,zapato,navidad]
def namestr(obj, namespase):
	return [name for name in namespase if namespase[name] is obj]




for n in items:
	if multivariable & n == n:
	    contenido.append(namestr(n, globals())[0])

print ("Los Reyes magos te han traido -->")
for n in contenido:
	print (n)




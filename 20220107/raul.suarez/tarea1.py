# Author: Raul Suarez
# Date: 01/10/2022

user_input = int(input("Enter a number between 0 and 255: "))
values = '{0:08b}'.format(user_input)

if values[0] == '1':
	print("CARRO")
else:
	pass

if values[1] == '1':
	print("CASA")
else:
	pass
	
if values[2] == '1':
	print("PERRO")
else:
	pass

if values[3] == '1':
	print("GATO")
else:
	pass
	
if values[4] == '1':
	print("PEZ")
else:
	pass
	
if values[5] == '1':
	print("MOTO")
else:
	pass
	
if values[6] == '1':
	print("ZAPATO")
else:
	pass

if values[7] == '1':
	print("NAVIDAD")
else:
	pass

print(f"\nYour input = [{values}]")
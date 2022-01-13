# BIS

# VARIABLES/OBJETOS DISPONIBLES

print("""

COSAS: 

Carro   ->  ON/OFF ->     1   
Casa    ->  ON/OFF ->     2
Perro   ->  ON/OFF ->     4
Gato    ->  ON/OFF ->     8
Pez     ->  ON/OFF ->    16
Moto    ->  ON/OFF ->    32
Zapato  ->  ON/OFF ->    64
Navidad ->  ON/OFF ->   128""")

V = ("Navidad","Zapato","Moto","Pez","Gato","Perro","Casa","Carro")

V = int(0)

print("\n")
if V == input("Ingresa un objeto: "):
    print("c muere")


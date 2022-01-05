import math

def obtenerDatos():
 #print ("Ingrese el numero de datos a tratar")
 #numdatos = int(input())
 datos = []
 #for i in range(0, numdatos):
 for i in range(0,7):
  print ("Ingrese el dato num ", i + 1)
  dato = input()
  datos.append(int(dato))
  print (dato)
 return datos

def obtenerPromedio(datos):
 suma = 0
 for dato in datos:
  suma += dato
 return suma / len(datos)

def obtenerVarianza(datos):
 n = len(datos)
 promedio = obtenerPromedio(datos)
 varianza = 0
 for dato in datos:
  varianza += math.pow((dato - promedio), 2)
 return varianza / (n - 1)

def main():
 salir = False
 datos = []
 varianza = 0

 while not salir:
  opcion = input()
  if(opcion == '1'):
   datos = obtenerDatos()
  elif(opcion == '2'):
   varianza = obtenerVarianza(datos)
   print ("Valor de varianza: ", varianza)
   #input("Enter para continuar...")
  elif(opcion == '3'):
   print ("Saliste")
   salir = True
  else:
   print ("No existe esa opción")

if __name__ == "__main__":
 main()

# Ejercicio de practica de Bits

Hacer un programa que guarde hasta 8 variables boleanas en un entero.

Las variables son:

* Carro   ->  on/off     1
* Casa    ->  on/off     2
* Perro   ->  on/off     4
* Gato    ->  on/off     8
* Pez     ->  on/off    16
* Moto    ->  on/off    32
* Zapato  ->  on/off    64
* Navidad ->  on/off   128


```
00000000  =  0
00000010  =  2  -> Casa
10001001  =  137  -> carro on, gato on, navidad on

multivariable = int(0)

carro = 1
navidad = 128

si multivariable  = carro hacer
  algo

si multivariable = navidad hacer
  otra cosa


si multivariable = carro y multivariable = pez y multivariable = navidad hacer
  un carro conducido por un pez en navidad

```

Para el miercoles antes de la case.

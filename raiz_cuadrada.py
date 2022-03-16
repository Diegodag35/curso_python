#Este programa calcula la raiz cuadrada de un numero 

from unicodedata import numeric


numero = int (input("La raiz cuadrada de:"))
raiz_cuadrada = numero **(1/2)
print(raiz_cuadrada)
#Escribe una función llamada mas_del_doble que reciba dos parámetros: num1 y num2. 
#La función debe retornar True si num2 es más del doble de num1. De lo contrario 
#debe retornar False.

def mas_del_doble(num1,num2):
    if num2 > 2*num1:
        return True
    else:
        return False

print(mas_del_doble(6,13))
#Escribe una función llamada gran_exponente que reciba dos parámetros: base y exponente. 
#Si base elevado a exponente es más de 5000 debe retornar True. De lo contrario debe 
#retornar False.

def gran_exponente(base,exponente):
    potencia = base ** exponente
    if potencia > 5000 :
        return True
    else:
        return False
print(gran_exponente(6,2))
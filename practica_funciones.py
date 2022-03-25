from math import factorial


def run():

    # def mi_funcion(param1,param2):
    #     print(param1)
    #     print(param2)

    # mi_funcion("hola",2)
    #función raiz cuadrada 
    # def raiz_nesima (exponente,potencia):
    #     resultado = potencia**(1/exponente)
    #     print("la raiz " + str(exponente) +" de "+ str(potencia) + " es: ", resultado)

   
    #factorial de un numero

    # numero = int(input("ingrese el numero "))
    # factorial = 1

    # for contador in range(1,(numero + 1)):
    #     factorial = factorial*contador
    #     contador += 1

    # print(str(numero) + "! = ", factorial)

    #practica del uso del return

    def valor_cuadrado(valor_x,valor_y):
        x_2 = valor_x**2
        y_2 = valor_y**2
        return x_2 , y_2

    x_2_cuadrado, y_2_cuadrado = valor_cuadrado(1,3)

    print(x_2_cuadrado , y_2_cuadrado)
    
 



if __name__ == "__main__":
    run()

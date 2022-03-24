from math import factorial


def run():

    # def mi_funcion(param1,param2):
    #     print(param1)
    #     print(param2)

    # mi_funcion("hola",2)
    #función raiz cuadrada 
    def raiz_nesima (exponente,potencia):
        resultado = potencia**(1/exponente)
        print("la raiz " + str(exponente) +" de "+ str(potencia) + " es: ", resultado)

   
    #factorial de un numero

    # numero = int(input("ingrese el numero "))
    # factorial = 1

    # for contador in range(1,(numero + 1)):
    #     factorial = factorial*contador
    #     contador += 1

    # print(str(numero) + "! = ", factorial)



if __name__ == "__main__":
    run()

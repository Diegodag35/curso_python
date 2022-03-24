def run():



    #factorial de un numero

    numero = int(input("ingrese el numero "))
    factorial = 1 

    for contador in range(1,(numero + 1)):
        factorial = factorial*contador
        contador += 1

    print(str(numero) + "! = ", factorial)
    







if __name__ == "__main__":
    run()
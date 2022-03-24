def run():



    #factorial de un numero

    numero = int(input("ingrese el numero ")) #el usuario ingresa el numero al cual desea sacar su factorial
    factorial = 1 #inicializamos factorial para evitar el prducto por cero
    for contador in range(1,(numero + 1)): #el segundo parametro le sumo 1 para que tome el valor de numnero incluido.
        factorial = factorial*contador  #operacion para guardar los productos
        contador += 1 #aumento de 1 por cada ciclo
    print(str(numero) + "! = ", factorial) 
    







if __name__ == "__main__":
    run()
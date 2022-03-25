# Proyecto 1. juego de adivinar el numero escogido por la computadora.

#necesito que el computador escoja un numero. se usa la biblioteca ramdom,
#con la función randint que e4scoje un numero entre un intervalo. 
import random 

def adivina_el_numero(limite_superior):
    print("Este es el juego adivina el número")
    print("La idea es adivinar el numero que fue escogido por la computadora")

    # el numero aleatorio escogido por la pc está entre 1 y limite_superior

    numero_pc = random.randint(1,limite_superior) 
    numero_inicial = int(input("adivine el numero de 1 a " + str(limite_superior) + " "))
    while numero_inicial != numero_pc:
        if numero_inicial > numero_pc:
            numero_inicial = int(input("ingrese un numero menor "))
        
        elif numero_inicial < numero_pc:
            numero_inicial = int(input("ingrese un numero mayor "))        
    
    print("¡ganador! el numero era " + str(numero_pc))

adivina_el_numero(50)















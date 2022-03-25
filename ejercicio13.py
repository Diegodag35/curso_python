#Escribe una función llamada calificar_pelicula que reciba un parámetro rating (un número). 
#Si el rating es menor a o igual a 5 la función debe retornar la cadena "Terrible!". Si el 
#rating está entre 5 y 9 debe retornar la cadena "Interesante". Si el rating es 9 o más debe 
#retornar la cadena "Increíble!".

def calificar_pelicula(raiting):
    if raiting <= 5:
        print("Terrible")

    elif raiting > 5 and raiting < 9:
        print("Interesante")

    elif raiting >= 9:
        print("Increible")

calificar_pelicula(9)
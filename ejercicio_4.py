#Escribe un programa que le pida al usuario su año de nacimiento e imprima su edad actual en la consola con la 
# frase "Tienes X años". Por ejemplo, asumiendo que el año actual es 2021 y el usuario ingresa 2000, el programa 
# debe imprimir en la consola: tienes 21 años

ano_actual = 2022
print("Ingrese el ano de nacimiento")
ano_nacimiento = int(input())
edad_actual = ano_actual - ano_nacimiento
print("tienes", edad_actual , "anos")
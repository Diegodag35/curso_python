#Este programa convirter temperatura de grados Fahrenheit a celsius


grados_fahrenheit = float(input("ingrese la temperatura en grados farhenheit: "))
grados_centigrados = (5/9)*(grados_fahrenheit - 32)
print("La temperatura de " + str(grados_fahrenheit) + "grados farhenheit a grados centigrados es de: ", grados_centigrados)
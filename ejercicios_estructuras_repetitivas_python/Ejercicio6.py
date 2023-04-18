#Escribir un programa que pida al usuario un número entero y muestre por pantalla un
#  triángulo rectángulo como el de más abajo, de altura el número introducido.

numero = input("Dime un numero entero por favor: ")
while numero.isdigit()== False:
    print("No es un numero lo que metiste ")
    numero = input("Dime un numero entero por favor: ")

numero = int(numero)

for i in range(numero):
    print("*"*(i+1))
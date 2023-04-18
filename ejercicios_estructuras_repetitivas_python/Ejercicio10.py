#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

numero = input("Dime un numero entero por favor: ")
while numero.isdigit()== False:
    print("No es un numero lo que metiste ")
    numero = input("Dime un numero entero por favor: ")
numero = int(numero)
if numero ==1:
    print("1 es primo")
else: 
    i = 2
    while numero % i != 0:
        i += 1
    if i == numero:
        print(str(numero) + " es primo")
    else:
        print(str(numero) + " no es primo")
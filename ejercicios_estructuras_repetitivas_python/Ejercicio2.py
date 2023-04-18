#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
edad = input("Dime tu edad: ")
while edad.isdigit() == False:
    print("No es un numero")
    edad = input("Dime tu edad: ")
edad = int(edad)
for i in range(edad):
    print(i+1)
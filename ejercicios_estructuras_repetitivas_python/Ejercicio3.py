#Escribir un programa que pida al usuario un número entero positivo y 
# muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

numero = input("Dime un numero entero positivo por favor: ")
while numero.isdigit()== False:
    print("No es un numero lo que metiste ")
    numero = input("Dime un numero entero por favor: ")

numero = int(numero)
output = "Los impares son: "
for i in range(1,numero+1):
    if i%2!=0:
        output += str(i)+", "

print(output[:len(output)-2])

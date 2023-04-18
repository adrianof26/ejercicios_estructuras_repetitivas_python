#Escribir un programa que pida al usuario un número entero positivo y 
# muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
numero = input("Dime un numero entero positivo por favor: ")
while numero.isdigit()== False:
    print("No es un numero lo que metiste ")
    numero = input("Dime un numero entero por favor: ")

numero = int(numero)
output = "La cuenta atras es: "
for i in range(numero):
    output += str(numero-i)+", "

print(output[:len(output)-2])
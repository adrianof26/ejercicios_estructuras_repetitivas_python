#Escribir un programa que pida al usuario una palabra y 
# luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

palabra = input("Deme una palabra que quiera dar la vuelta y ver letra por letra: ")
while palabra.isalpha() == False:
    print("No es una palabra")
    palabra = str(input("Deme una palabra: "))
for i in range(len(palabra)):
    print(palabra[len(palabra)-i-1])

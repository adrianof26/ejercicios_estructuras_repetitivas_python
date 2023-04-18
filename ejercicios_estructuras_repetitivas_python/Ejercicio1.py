#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
palabra = input("Deme una palabra que quiera repetir: ")
while palabra.isalpha() == False:
    print("No es una palabra")
    palabra = str(input("Deme una palabra que quiera repetir: "))
for i in range(10):
    print(palabra)
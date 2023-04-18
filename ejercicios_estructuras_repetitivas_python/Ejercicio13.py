#Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba "salir" que terminará.
print("Bienvenido a la cueva")
frase = input("Escuchas eco hasta que dices salir: ")
while frase != "salir":
    print(frase)
    frase = input("Deme una frase: ")

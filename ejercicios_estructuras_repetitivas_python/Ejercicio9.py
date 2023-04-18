#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
# pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
print("Bienvenido a su pagina de seguridad")
password = input("Introduzca su contraseña : ")
password2 = input("Repita su contraseña a ver si no se equivoca: ")
while password != password2:
    print("No son iguales")
    password = input("Introduzca su contraseña : ")
    password2 = input("Repita su contraseña a ver si no se equivoca: ")
print("Bien hecho ya puede acceder")
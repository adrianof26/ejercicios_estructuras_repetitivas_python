#Escribir un programa que pregunte al usuario una cantidad a invertir, 
#el interés anual y el número de años, y muestre por pantalla el capital obtenido 
#en la i nversión cada año que dura la inversión.

cantidad = input("Dime la cantidad a invertir: ")
cantidad_cleaned = cantidad.replace(",",".")
cantidad_cleaned = cantidad_cleaned.replace(".","")

while cantidad_cleaned.isdigit() == False:
    print("No es un numero lo que has introducido")
    cantidad = input("Dime bien la cantidad que quieres invertir: ")
    cantidad_cleaned = cantidad.replace(",",".")
    cantidad_cleaned = cantidad_cleaned.replace(".","")
cantidad = cantidad.replace(",",".")
cantidad = float(cantidad)

interes = input("Dime el interes anual: ")
interes_cleaned = interes.replace(",",".")
interes_cleaned = interes_cleaned.replace(".","")

while interes_cleaned.isdigit() == False:
    print("No es un buen interes lo que has introducido")
    interes = input("Dime bien el interes anual: ")
    interes_cleaned = interes.replace(",",".")
    interes_cleaned = interes_cleaned.replace(".","")
interes = interes.replace(",",".")
interes = float(interes)/100

años = input("Dime el numero de años: ")

while años.isdigit() == False:
    print("No es un año valido lo que has introducido")
    años = input("Dime bien el numero de años: ")

años = int(años)

for i in range(años):
    cantidad = cantidad + cantidad*interes
    cantidad = round(cantidad,2)
    print("El capital obtenido en el año",i+1,"es de",cantidad)

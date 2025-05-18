from mate import *

print("calcula perimetro:")

radio = float(input("introduce el radio: "))

print(f"el perimetro es: {perimetro(radio)}")

print("calcula la raiz: ")

numero = float(input("Intoduce el numero: "))
indice = int(input("Intruduce el indice: "))

print(f"la raiz es: {raiz(numero, indice)}")


print("Calcula la hipotenusa: ")

cateto1 = float(input("Intruduce el cateto 1: "))
cateto2 = float(input("Introduce el cateto 2: "))

print(f"La hipotenusa es: {hipotenusa(cateto1, cateto2)}")
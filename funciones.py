def saludar(): #string:
    saludo = "Hola, Como estas"
    return saludo
saludar_1 = saludar()
print(saludar_1)

def saludar_personalizado(usuario): #void:
    saludo = f"Hola {usuario} como estas"
    print(saludo)
    
nombre = input("Dime tu nombre: ")
saludar_personalizado(usuario=nombre)
saludar_personalizado(nombre)
    




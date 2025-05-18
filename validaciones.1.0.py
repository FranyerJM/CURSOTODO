def formatear_cedula (cedula):
    cedula = cedula.replace ("V", "").replace("v", "")
    cedula =cedula.replace("-", "").replace(".", "").replace(",", "")

    if not cedula.isdigit() or len(cedula) < 7:
        return "Cedula invalida"
    return cedula

print(formatear_cedula("V-7.456.789"))

print(formatear_cedula("V-7.456.89"))

def correo_valido (correo):
    tiene_arroba = False
    tiene_punto_despues = False
    posicion_arroba = -1

    for i in range (len(correo)):
         if correo[i] == "@":
             tiene_arroba = True
             posicion_arroba = i
             break
    if not tiene_arroba:
        print(f"usuario {correo} - Verificacion invalida")
    
    for i in range(posicion_arroba + 1, len(correo)):
        if correo[i] == ".":
            tiene_punto_despues = True
            break
    if posicion_arroba == 0 or posicion_arroba == len(correo) -1:
        print(f"usuario {correo} - verificacion invalida")
        return
    if not tiene_punto_despues:
        print(f"usuario {correo} - verificacion invalida")
        return
    print(f"usuario {correo} Verificacion Valida")

correo_valido("Robertocarlos@gmail.com")
correo_valido("Robertocarlos@gmailcom")
correo_valido("Robertocarlosgmail.com")
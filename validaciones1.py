def formatear_cedula(cedula):
    if "V" in cedula or "v" in cedula :
        ci = cedula[1:] 
        
    if "-" in cedula:
        try:
            ci = ci[1:]
        except:
            ci = cedula[1:]
    
    if "." in cedula:
        try:
            ci = ci.split(".")
        except:
            ci = cedula.split(".")
        return ci[0] + ci[1] + ci[2]
    
    if "," in cedula:
        ci = ci.split(",")
        return ci[0] + ci[1] + ci[2]
    
    if len(ci) < 7:
        return "Cedula no valida"
    
    return ci 
        
print(formatear_cedula("10.739.234"))

def correo_valido(correo):
    tiene_arroba = False
    tiene_punto_despues = False
    posicion_arroba = -1

    for i in range(len(correo)):
        if correo[i] == "@":
            tiene_arroba = True
            posicion_arroba = i
            break

    if not tiene_arroba:
        print(f"Usuario {correo} - Verificación inválida")
        return

    for i in range(posicion_arroba + 1, len(correo)):
        if correo[i] == ".":
            tiene_punto_despues = True
            break

    if posicion_arroba == 0 or posicion_arroba == len(correo) - 1:
        print(f"Usuario {correo} - Verificación inválida")
        return

    if not tiene_punto_despues:
        print(f"Usuario {correo} - Verificación inválida")
        return

    print(f"Usuario {correo} - Verificación válida")

correo_valido("robertocarlos@gmai.com")
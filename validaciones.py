def formatear_cedula(cedula):
    if "V" in cedula or "v" in cedula :
        ci = cedula[1:] 
        
    if "-" in cedula:
        ci = ci[1:]
    
    if "." in cedula:
        ci = ci.split(".")
        return ci[0] + ci[1] + ci[2]
    
    if "," in cedula:
        ci = ci.split(",")
        return ci[0] + ci[1] + ci[2]
    
    if len(ci) < 7:
        return "Cedula no valida"
    
    return ci 
        
print(formatear_cedula("V-7.345.456"))

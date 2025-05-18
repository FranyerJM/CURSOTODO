from zodiaco_logica import obtener_signo_zodiaco
def main():
    fecha = input("Introduce tu fecha de nacimieeto (DD/MM/AAAA): ")
    try:
        partes = fecha.split("/")
        dia = int(partes[0])
        mes = int(partes[1])
        if dia > 31:
            print("La fecha proporcionada no es valida. ")
        else:
            signo = obtener_signo_zodiaco(dia, mes)
            print("Tu signo dal zodiaco es: ", signo)
    except:
        print("Fecha invalida.")    
        

main()
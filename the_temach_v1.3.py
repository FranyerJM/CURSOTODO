import datetime as dt

class Utiles:
    def __init__(self, fecha_de_fran, fecha_de_rachel):
        self.fecha_de_fran = fecha_de_fran
        self.fecha_de_rachel = fecha_de_rachel
        self.resta = fecha_de_rachel - fecha_de_fran
        
    def cuanto_te_ignoro(self):
        hora = self.resta.seconds // 3600
        minutos = (self.resta.seconds // 60) % 60
        dia = self.resta.days
        print (f'\n\nTe ignoro: {dia} dias, {hora} horas y {minutos} minutos')
    
    def cuando_le_vas_a_responder(self):
        tiempo_a_ignorar = self.resta * 2 
        self.fecha_a_responder = fecha_de_rachel + tiempo_a_ignorar 
    
    def final(self):
        fecha_a_responder = self.fecha_a_responder
        dia = fecha_a_responder.strftime("%d")
        mes = fecha_a_responder.strftime("%m")
        anio = fecha_a_responder.strftime("%Y")
        hora = fecha_a_responder.strftime("%I:%M %p")
        meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
        print (f'\n\nLe vas a responder el {dia} de {meses[int(mes)-1]} del {anio} a las {hora}\n\n')
        
    def ejecutar(self):
        self.cuanto_te_ignoro()
        self.cuando_le_vas_a_responder()
        self.final()
        
def fran():
    dia = int(input("Que dia le escribiste: "))
    mes = int(input("Que mes le escribiste: "))
    anio = int(input("Que año le escribiste: "))
    hora = int(input("Que hora le escribiste: "))
    minutos = int(input("Que minutos le escribiste: "))
    
    fecha_de_fran = dt.datetime(anio, mes, dia, hora, minutos)
    return fecha_de_fran

def rachel():
    dia = int(input("\nQue dia respondio: "))
    mes = int(input("Que mes respondio: "))
    anio = int(input("Que año respondio: "))
    hora = int(input("Que hora respondio: "))
    minutos = int(input("Que minuto respondio: "))
    global fecha_de_rachel
    fecha_de_rachel = dt.datetime(anio, mes, dia, hora, minutos)
    return fecha_de_rachel

utiles = Utiles(fran(), rachel())

utiles.ejecutar()
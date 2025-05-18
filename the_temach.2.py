import datetime as dt
import vlc
import tkinter as tk

global fecha_de_rachel
fecha_de_rachel = None

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

def cuanto_te_ignoro():
    fecha_de_fran = fran()
    fecha_de_rachel = rachel()
    resta = fecha_de_rachel - fecha_de_fran
    hora = resta.seconds // 3600
    minutos = (resta.seconds // 60) % 60
    dia = resta.days
    print (f'\n\nTe ignoro: {dia} dias, {hora} horas y {minutos} minutos')
    return resta
  
def cuando_le_vas_a_responder():
    tiempo_a_ignorar = cuanto_te_ignoro() * 2 
    fecha_a_responder = fecha_de_rachel + tiempo_a_ignorar 
    return fecha_a_responder

def reproducir_vlc(ruta_video):
    root = tk.Tk()
    root.title("Reproducir con VLC")
    
    instance = vlc.Instances()
    player = instance.media_player_new()
    media = instance.media_new(ruta_video)
    player.set_media(media)
    
    frame = tk.Frame(root, width=800, height=600)
    frame.pack(fill=tk.BOTH, expand=1)
    
    
    def iniciar_video():
        player.set_hwnd(frame.winfo_id())
        player.play()

    root.after(100, iniciar_video)
    root.mainloop()

def final():
    fecha_a_responder = cuando_le_vas_a_responder()
    dia = fecha_a_responder.strftime("%d")
    mes = fecha_a_responder.strftime("%m")
    anio = fecha_a_responder.strftime("%Y")
    hora = fecha_a_responder.strftime("%I:%M %p")
    meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    print (f'\n\nLe vas a responder el {dia} de {meses[int(mes)-1]} del {anio} a las {hora}\n\n')
   
    if cuanto_te_ignoro() > dt.timedelta(days=3):
        print ('\nSe acabo')
    reproducir_vlc(r"mandelalavrg.mp4")   


final()
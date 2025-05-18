class Cancion():
    def __init__ (self, nombre, artista, duracion, genero):
        self.nombre = nombre
        self.artista = artista
        self.duracion = duracion 
        self.genero = genero
        
    def listas(self):
        print(f'nombre: {self.nombre}')
        
    def reproducir(self):
        print(f'Reproduciendo {self.nombre} de {self.artista} y tiene una duracion de {self.duracion} minutos')
    
    def pausar(self):
        print(f'Pausando {self.nombre} de {self.artista}')
        
Cancion1 = Cancion('Despacito', 'Luis Fonsi', 3, 'Pop')
Cancion2 = Cancion('Shape of You', 'Ed Sheeran', 4, 'Pop')
Cancion3 = Cancion('Blinding Lights', 'The Weeknd', 4, 'Pop')
Cancion4 = Cancion('Bad Guy', 'Billie Eilish', 3, 'Pop')
Cancion5 = Cancion('Levitating', 'Dua Lipa', 3, 'Pop')
Cancion6 = Cancion('Despasito Remix', 'Luis Fonsi', 3, 'Pop')
cancion7 = Cancion('Vailame', 'Luis Fonsi', 3, 'Pop')

Cancion1.reproducir()      
lista_canciones = [Cancion1, Cancion2, Cancion3, Cancion4, Cancion5]

class Playlist():
    def __init__ (self, nombre_playlist, lista_canciones):
        self.nombre_playlist = nombre_playlist
        self.lista_canciones = lista_canciones

    def listar_por_artista(self, artista):
        playlist = []
        for i in lista_canciones:
            if i.artista == artista:
                playlist.append(i)
                
        return playlist
                
playlist = Playlist('Mi playlist', lista_canciones)
print(playlist.listar_por_artista('Luis Fonsi')[0].reproducir())
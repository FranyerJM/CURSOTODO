from csv import DictWriter

def exportar_csv(datos_export, nombre_archivo): 
    
    with open(nombre_archivo, 'w', newline='') as archivo_csv:

        escritor = DictWriter(archivo_csv, fieldnames=datos_export[0].keys(), delimiter=';')
        escritor.writeheader()
        escritor.writerows(datos_export)
        

lista = [
    {
        'nombre': 'Juan',
        'apellido': 'Perez',
        'edad': 25,
        'cedula': 123456789,
        'pago': 10
    },
    {
        'nombre': 'Ana',
        'apellido': 'Gomez',
        'edad': 30,
        'cedula': 987654321,
        'pago': 15
    }
]

nombre_archivo = 'users.csv'

#exportar_csv(lista, nombre_archivo)


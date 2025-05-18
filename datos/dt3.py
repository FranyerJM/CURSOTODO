import csv

with open("archivo.csv") as file:
    reader = csv.reader(file)
    next(reader) # Descartamos cabecera
    nuevo_dict = dict(reader)
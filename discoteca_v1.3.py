from dict_csv import exportar_csv

def get_client_data():
    """Collects and returns client information"""
    nombre_apellido = input('Ingrese tu nombre y apellido: ')
    orden = nombre_apellido.split(' ')
    nombre = orden[0]
    apellido = orden[1]  
    edad = int(input('Ingrese su edad: '))
    cedula = int(input('Ingrese su cedula: '))
    pago = int(input('Ingrese su pago: '))
    
    return {
        'nombre': nombre,
        'apellido': apellido,
        'edad': edad,
        'cedula': cedula,
        'pago': pago
    }

def validate_entry(edad, pago):
    """Validates if client can enter based on age and payment"""
    if edad >= 18 and pago >= 10:
        print('Bienvenido a la discoteca')
        return True
    else:
        print('No puede ingresar a la discoteca')
        return False

def calculate_demand(suma_pagos):
    """Determines and prints demand level based on total payments"""
    if suma_pagos <= 200:
        print(f'La demanda de la discoteca es baja, la suma de los pagos es: {suma_pagos}')  
    elif suma_pagos > 200 and suma_pagos <= 500:
        print(f'La demanda de la discoteca es media, la suma de los pagos es: {suma_pagos}')
    else:
        print(f'La demanda de la discoteca es alta, la suma de los pagos es: {suma_pagos}')
        
def formatear_diccionario(diccionario):
    """Formats the dictionary for CSV export"""
    return [{'nombre': cliente['nombre'],
             'apellido': cliente['apellido'],
             'edad': cliente['edad'],
             'cedula': cliente['cedula'],
             'pago': cliente['pago']} for cliente in diccionario.values()]

def main():
    """Main program function"""
    clientes = []
    suma_pagos = 0
    diccionario = {}
    
    cantidad_de_clientes = int(input('Cantidad de clientes: ')) 
    
    for _ in range(cantidad_de_clientes):
        cliente = get_client_data()
        diccionario[str(cliente['cedula'])] = cliente
        
        if validate_entry(cliente['edad'], cliente['pago']):
            clientes.append([
                cliente['nombre'],
                cliente['apellido'],
                cliente['edad'],
                cliente['cedula'],
                cliente['pago']
            ])
            suma_pagos += cliente['pago']
    
    calculate_demand(suma_pagos)
    
    clientes_que_ingresaron = len(clientes)
    clientes_que_no_ingresaron = cantidad_de_clientes - clientes_que_ingresaron
    
    print(f'Clientes que ingresaron: {clientes_que_ingresaron}')
    print(f'Clientes que no ingresaron: {clientes_que_no_ingresaron}')
    print(diccionario)
    exportar_csv(formatear_diccionario(diccionario), 'clientes.csv')
if __name__ == '__main__':
    main()
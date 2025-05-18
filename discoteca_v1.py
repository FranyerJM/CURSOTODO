# Description: Programa que permite el  ingreso a una discoteca a personas mayores de 18 años y que paguen 10 dolares
clientes = []
suma_pagos = 0
cantidad_de_clientes = int(input('Cantidad de clientes: ')) 
for i in range (cantidad_de_clientes):
    nombre_apellido = input('Ingrese tu nombre y apellido: ')
    orden  = nombre_apellido.split(' ')
    nombre = orden [0]
    apellido = orden [1]  
    edad = int(input('Ingrese su edad: '))
    cedula = int(input('Ingrese su cedula: '))
    pago = int(input('Ingrese su pago: '))
    cliente = [nombre, apellido, edad, cedula, pago]
    
    if edad >= 18 and pago >= 10:
        clientes.append(cliente)
        suma_pagos += pago
        print ('Bienvenido a la discoteca')
    else:
        print ('No puede ingresar a la discoteca')
      
if suma_pagos <= 200:
    print (f'La demanda de la discoteca es baja, la suma de los pagos es: {suma_pagos}')  
elif suma_pagos > 200 and suma_pagos <= 500:
    print (f'La demanda de la discoteca es media, la suma de los pagos es: {suma_pagos}')
elif suma_pagos > 500:
    print (f'La demanda de la discoteca es alta, la suma de los pagos es: {suma_pagos}')
clientes_que_ingresaron = len(clientes)
clientes_que_no_ingresaron = cantidad_de_clientes - clientes_que_ingresaron
print (f'Clientes que ingresaron: {clientes_que_ingresaron}')
print (f'Clientes que no ingresaron: {clientes_que_no_ingresaron}')
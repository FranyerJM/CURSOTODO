colores = ['rojo', 'azul', 'verde']

print(len(colores))
print(colores)

colores.append('amarillo')
print(len(colores))
print(colores)

colores[2] = 'rosa'
print(colores)

print('cambios')
colores[1:2] = ''
print(colores)


colores[1:2] = ''
print(colores)

saludo = 'HoLa CoMo EsTaS'
secuencia = '1,3,5,7,11'

lista_de_primos = secuencia.split(',')
print(lista_de_primos)

lista_de_palabras = saludo.split(' ')
print(lista_de_palabras)

cambio_saludo = saludo.lower()
print(f'uso de upper.. {cambio_saludo}')
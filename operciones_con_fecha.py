import datetime as dt

ya = dt.datetime.now()
print(ya)

ya_formateada = ya.strftime("%d-%m-%y %H:%M")
print(ya_formateada)

ya_dia = ya.strftime("%d")

# ya_day = ya.month()
# print(ya_day)

tiempo = ya + dt.timedelta(weeks=52, days=1)

print(tiempo)
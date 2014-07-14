#!/usr/bin/python

visitas_diarias = int(input("¿Cuántas visitas ha habido hoy en tu Web?: "))

mensaje = "¡Muchas visitas!" if (visitas_diarias > 1400) else "¡Pocas visitas!"

print("Hoy tenemos en nuestra Web %s visitas." % visitas_diarias, mensaje)
import mysql.connector

cnx = mysql.connector
cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='myprueba')
c = cnx.cursor()

c.execute("""create table empleados(dni text, nombre text, departamento text)""")
c.execute("""insert into empleados values('123345678-A', 'Alfonso Ruiz', 'Contabilidad')""")
cnx.commit()


cnx.close()

